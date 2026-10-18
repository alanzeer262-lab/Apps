#!/usr/bin/env python3
"""Transcribe narration with word timestamps and align scene changes to spoken anchors.

The render is intentionally blocked if an anchor cannot be found confidently.
No proportional scaling or guessed storyboard timings are used.
"""
from __future__ import annotations

import json
import os
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

import av
from faster_whisper import WhisperModel

ROOT = Path(__file__).resolve().parents[1]
AUDIO_DIR = ROOT / "public" / "audio"
CUES_PATH = Path(os.environ.get("PYLEARN_SYNC_CUES", str(ROOT / "scripts" / "sync-cues.json")))
OUTPUT_PATH = Path(os.environ.get("PYLEARN_ALIGNMENT_OUTPUT", str(ROOT / "src" / "generated-alignment.json")))
TRANSCRIPT_JSON_PATH = ROOT / "out" / "lesson-01" / "transcript.json"
TRANSCRIPT_TEXT_PATH = ROOT / "out" / "lesson-01" / "transcript.txt"
_DEFAULT_AUDIO_FILES = [
    "public/audio/lesson-01/part-01.mp3",
    "public/audio/lesson-01/part-02.mp3",
]
_AUDIO_FILE_VALUES = [value.strip() for value in os.environ.get("PYLEARN_AUDIO_FILES", ",".join(_DEFAULT_AUDIO_FILES)).split(",") if value.strip()]
AUDIO_FILES = [Path(value) if Path(value).is_absolute() else ROOT / value for value in _AUDIO_FILE_VALUES]


def audio_duration(path: Path) -> float:
    with av.open(str(path)) as container:
        if container.duration is not None:
            # PyAV container.duration is expressed in AV_TIME_BASE units (microseconds).
            return float(container.duration / av.time_base)
        stream = next((s for s in container.streams if s.type == "audio"), None)
        if stream is None or stream.duration is None or stream.time_base is None:
            raise RuntimeError(f"Cannot measure audio duration: {path.name}")
        return float(stream.duration * stream.time_base)


def tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def transcribe_tracks(model: WhisperModel, files: list[Path]) -> tuple[list[dict], list[float]]:
    words: list[dict] = []
    offsets: list[float] = []
    offset = 0.0

    for path in files:
        if not path.is_file():
            raise RuntimeError(f"Missing narration file: {path}")
        offsets.append(offset)
        duration = audio_duration(path)
        print(f"Transcribing {path.name} ({duration:.3f}s) at timeline offset {offset:.3f}s")
        segments, info = model.transcribe(
            str(path),
            language="en",
            beam_size=5,
            word_timestamps=True,
            vad_filter=False,
            condition_on_previous_text=True,
        )
        segment_count = 0
        for segment in segments:
            segment_count += 1
            if segment.words:
                for word in segment.words:
                    word_tokens = tokens(word.word)
                    if not word_tokens:
                        continue
                    words.append({
                        "text": word.word.strip(),
                        "token": " ".join(word_tokens),
                        "start": offset + max(0.0, float(word.start)),
                        "end": offset + min(duration, float(word.end)),
                    })
            else:
                # Defensive fallback; word_timestamps normally supplies words.
                for token in tokens(segment.text):
                    words.append({
                        "text": token,
                        "token": token,
                        "start": offset + float(segment.start),
                        "end": offset + float(segment.end),
                    })
        print(f"  language={info.language}, segments={segment_count}")
        offset += duration

    words.sort(key=lambda item: item["start"])
    if not words:
        raise RuntimeError("Transcription returned no words.")
    return words, offsets


def align_anchor(anchor: str, words: list[dict], cursor: int = 0, min_time: float = 0.0, max_time: float | None = None) -> dict:
    wanted = tokens(anchor)
    if not wanted:
        raise ValueError(f"Empty anchor: {anchor!r}")

    # Search windows near the expected phrase length; scoring is lexical, not
    # proportional-to-runtime. The cursor prevents reusing an earlier phrase.
    min_len = max(1, len(wanted) - 2)
    max_len = len(wanted) + 3
    target = " ".join(wanted)
    best = None

    for start_i in range(cursor, len(words)):
        for window_len in range(min_len, max_len + 1):
            end_i = start_i + window_len
            if end_i > len(words):
                continue
            candidate_words = words[start_i:end_i]
            if candidate_words[0]["start"] < min_time:
                continue
            if max_time is not None and candidate_words[-1]["end"] > max_time:
                continue
            candidate = " ".join(w["token"] for w in candidate_words)
            ratio = SequenceMatcher(None, target, candidate).ratio()
            target_set = set(wanted)
            candidate_set = set(candidate.split())
            overlap = len(target_set & candidate_set) / max(1, len(target_set))
            score = 0.78 * ratio + 0.22 * overlap
            if best is None or score > best["score"]:
                best = {
                    "startIndex": start_i,
                    "endIndex": end_i,
                    "start": candidate_words[0]["start"],
                    "end": candidate_words[-1]["end"],
                    "score": score,
                    "matched": " ".join(w["text"] for w in candidate_words),
                }

    if best is None:
        raise RuntimeError(f"No transcript window available for anchor: {anchor!r}")
    return best


def main() -> None:
    cues = json.loads(CUES_PATH.read_text(encoding="utf-8"))
    confidence_floor = float(cues.get("minimumConfidence", 0.62))
    model_name = cues.get("model", "tiny.en")
    print(f"Loading Whisper model {model_name!r} (CPU/int8)")
    model = WhisperModel(model_name, device="cpu", compute_type="int8", cpu_threads=2, num_workers=1)
    words, offsets = transcribe_tracks(model, AUDIO_FILES)
    durations = [audio_duration(path) for path in AUDIO_FILES]
    total_duration = sum(durations)

    cursor = 0
    aligned = []
    for cue in cues["scenes"]:
        match = align_anchor(cue["anchor"], words, cursor)
        if match["score"] < confidence_floor:
            raise RuntimeError(
                f"Low-confidence sync anchor for scene {cue['id']}: "
                f"{match['score']:.3f} < {confidence_floor:.3f}; "
                f"expected={cue['anchor']!r}; matched={match['matched']!r}. "
                "Update the cue to match the recording; do not guess a timestamp."
            )
        aligned.append({
            "id": int(cue["id"]),
            "anchor": cue["anchor"],
            "matched": match["matched"],
            "confidence": round(match["score"], 3),
            "anchorStart": round(match["start"], 3),
        })
        cursor = max(match["startIndex"] + 1, match["endIndex"] - 2)
        print(f"Scene {cue['id']:02d}: {match['start']:.2f}s "
              f"(confidence {match['score']:.2f}) — {match['matched']}")

    expected_scene_count = len(cues["scenes"])
    if len(aligned) != expected_scene_count:
        raise RuntimeError(f"Expected {expected_scene_count} scene anchors, got {len(aligned)}")
    if aligned[0]["anchorStart"] > 3.0:
        raise RuntimeError("First scene anchor is unusually late; inspect the narration/cues.")
    starts = [0.0] + [entry["anchorStart"] for entry in aligned[1:]]
    for i in range(1, len(starts)):
        if starts[i] <= starts[i - 1]:
            raise RuntimeError(f"Non-monotonic scene timing at scene {i + 1}")
        if starts[i] - starts[i - 1] < 2.5:
            raise RuntimeError(
                f"Scene {i + 1} begins only {starts[i] - starts[i - 1]:.2f}s after "
                f"scene {i}; review the matched anchor phrases."
            )

    scene_timings = []
    cue_by_id = {int(cue["id"]): cue for cue in cues["scenes"]}
    for i, entry in enumerate(aligned):
        start = starts[i]
        end = starts[i + 1] if i + 1 < len(starts) else total_duration
        if end <= start:
            raise RuntimeError(f"Invalid scene interval for scene {entry['id']}")
        timing = {
            **entry,
            "start": round(start, 3),
            "end": round(end, 3),
        }
        code_anchor = cue_by_id[entry["id"]].get("codeAnchor")
        if code_anchor:
            scene_words = tokens(entry["anchor"])
            code_words = tokens(code_anchor)
            if scene_words[:len(code_words)] == code_words:
                timing["codeAt"] = round(start, 3)
            else:
                code_match = align_anchor(code_anchor, words, cursor=0, min_time=start + 0.3, max_time=end - 0.25)
                if code_match["score"] < confidence_floor:
                    raise RuntimeError("Low-confidence code anchor for scene " + str(entry["id"]) + ": " + repr(code_anchor) + " matched " + repr(code_match["matched"]))
                timing["codeAt"] = round(code_match["start"] + 0.1, 3)
                timing["codeMatched"] = code_match["matched"]
                timing["codeConfidence"] = round(code_match["score"], 3)
                print("  code scene " + str(entry["id"]) + ": " + str(timing["codeAt"]) + "s")
        error_anchor = cue_by_id[entry["id"]].get("errorAnchor")
        if error_anchor:
            error_match = align_anchor(error_anchor, words, cursor=0, min_time=start + 1.0, max_time=end - 0.25)
            if error_match["score"] < confidence_floor:
                raise RuntimeError("Low-confidence error anchor for scene " + str(entry["id"]) + ": " + repr(error_anchor) + " matched " + repr(error_match["matched"]))
            timing["errorAt"] = round(error_match["start"] + 0.1, 3)
            timing["errorMatched"] = error_match["matched"]
            timing["errorConfidence"] = round(error_match["score"], 3)
            print("  error scene " + str(entry["id"]) + ": " + str(timing["errorAt"]) + "s")
        fix_anchor = cue_by_id[entry["id"]].get("fixAnchor")
        if fix_anchor:
            fix_match = align_anchor(fix_anchor, words, cursor=0, min_time=start + 1.0, max_time=end - 0.25)
            if fix_match["score"] < confidence_floor:
                raise RuntimeError("Low-confidence correction anchor for scene " + str(entry["id"]) + ": " + repr(fix_anchor) + " matched " + repr(fix_match["matched"]))
            timing["fixAt"] = round(fix_match["start"] + 0.1, 3)
            timing["fixMatched"] = fix_match["matched"]
            timing["fixConfidence"] = round(fix_match["score"], 3)
            print("  correction scene " + str(entry["id"]) + ": " + str(timing["fixAt"]) + "s")
        output_anchor = cue_by_id[entry["id"]].get("outputAnchor")
        if output_anchor:
            output_match = align_anchor(
                output_anchor,
                words,
                cursor=0,
                min_time=start + 1.0,
                max_time=end - 0.25,
            )
            if output_match["score"] < confidence_floor:
                raise RuntimeError(
                    f"Low-confidence output anchor for scene {entry['id']}: "
                    f"{output_match['score']:.3f} < {confidence_floor:.3f}; "
                    f"expected={output_anchor!r}; matched={output_match['matched']!r}."
                )
            output_edge = cue_by_id[entry["id"]].get("outputEdge", "start")
            output_time = output_match["end"] if output_edge == "end" else output_match["start"]
            timing["outputAt"] = round(output_time + 0.1, 3)
            timing["outputAnchor"] = output_anchor
            timing["outputMatched"] = output_match["matched"]
            timing["outputConfidence"] = round(output_match["score"], 3)
            print(f"  output scene {entry['id']:02d}: {timing['outputAt']:.2f}s "
                  f"(confidence {output_match['score']:.2f})")
        for key in ("codeAt", "outputAt", "errorAt", "fixAt"):
            if key in timing and not (start <= timing[key] < end):
                raise RuntimeError("Event " + key + " for scene " + str(entry["id"]) + " falls outside its scene interval.")
        if "errorAt" in timing and "fixAt" in timing and timing["fixAt"] <= timing["errorAt"]:
            raise RuntimeError("Correction event occurs before the error in scene " + str(entry["id"]))
        if "codeAt" in timing and "outputAt" in timing and timing["outputAt"] < timing["codeAt"]:
            raise RuntimeError("Output is scheduled before code appears in scene " + str(entry["id"]))
        scene_timings.append(timing)

    TRANSCRIPT_JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    transcript_payload = {
        "generatedBy": "faster-whisper (Whisper) in GitHub Actions",
        "model": model_name,
        "language": "en",
        "durationSeconds": round(total_duration, 3),
        "audioFiles": [path.relative_to(ROOT).as_posix() for path in AUDIO_FILES],
        "words": words,
    }
    TRANSCRIPT_JSON_PATH.write_text(json.dumps(transcript_payload, indent=2) + "\\n", encoding="utf-8")
    transcript_lines = [f"[{word['start']:.3f}-{word['end']:.3f}] {word['text']}" for word in words]
    TRANSCRIPT_TEXT_PATH.write_text("\\n".join(transcript_lines) + "\\n", encoding="utf-8")
    print(f"Wrote {TRANSCRIPT_JSON_PATH.relative_to(ROOT)}")
    print(f"Wrote {TRANSCRIPT_TEXT_PATH.relative_to(ROOT)}")

    payload = {
        "generated": True,
        "model": model_name,
        "durationSeconds": round(total_duration, 3),
        "part2StartSeconds": round(durations[0], 3),
        "audioTracks": [
            {"src": "/" + path.relative_to(ROOT).as_posix(), "start": round(offsets[index], 3)}
            for index, path in enumerate(AUDIO_FILES)
        ],
        "scenes": scene_timings,
    }
    OUTPUT_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH.relative_to(ROOT)}")
    print(f"Timeline duration: {total_duration:.3f}s; part 2 starts at {durations[0]:.3f}s")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
