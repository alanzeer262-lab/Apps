#!/usr/bin/env python3
"""Transcribe narration, then align scenes and visual events to spoken phrase anchors."""
from __future__ import annotations
import difflib, json, re, sys
from pathlib import Path
import av
from faster_whisper import WhisperModel

ROOT = Path(__file__).resolve().parents[1]
AUDIO_FILES = [ROOT / "public/audio/lesson-01/part-01.mp3", ROOT / "public/audio/lesson-01/part-02.mp3"]
STORYBOARD = ROOT / "docs/LESSON_01_REVISED_STORYBOARD.json"
CUES = ROOT / "scripts/sync-cues.revised-draft.json"
TRANSCRIPT_JSON = ROOT / "out/lesson-01/transcript.json"
TRANSCRIPT_TEXT = ROOT / "out/lesson-01/transcript.txt"
ALIGNMENT = ROOT / "src/generated-alignment.json"
TOKEN_RE = re.compile(r"[a-z0-9]+")

def toks(s):
    value = s.lower().replace("pylearn", "py learn")
    return TOKEN_RE.findall(value)

def duration(path):
    with av.open(str(path)) as c:
        if c.duration is not None:
            return c.duration / av.time_base
        st = next((x for x in c.streams if x.type == "audio"), None)
        if st is None or st.duration is None or st.time_base is None:
            raise RuntimeError(f"Cannot measure audio duration: {path}")
        return float(st.duration * st.time_base)

def best_phrase_match(words, phrase, min_time=0.0, max_time=float("inf")):
    target = toks(phrase)
    if not target:
        raise RuntimeError(f"Empty phrase anchor: {phrase!r}")
    candidates = []
    for i, word in enumerate(words):
        if word["start"] < min_time:
            continue
        if word["start"] >= max_time:
            break
        for size in range(max(1, len(target)-2), len(target)+4):
            chunk = words[i:i+size]
            if not chunk or chunk[-1]["end"] > max_time:
                continue
            observed = []
            for item in chunk:
                observed.extend(toks(item["text"]))
            score = difflib.SequenceMatcher(None, target, observed, autojunk=False).ratio()
            score -= abs(len(target)-len(observed))*0.015
            candidate = (score, i, chunk[0]["start"], chunk[-1]["end"])
            if not candidates or candidate[0] > candidates[0][0]:
                candidates = [candidate]
            elif candidate[0] == candidates[0][0]:
                candidates.append(candidate)
    if not candidates:
        return None
    # In case of equal matches, use the earliest occurrence in the allowed range.
    return max(candidates, key=lambda item: (item[0], -item[1]))

def require_match(words, phrase, min_time, max_time, context):
    match = best_phrase_match(words, phrase, min_time, max_time)
    if match is None or match[0] < 0.70:
        score = 0.0 if match is None else match[0]
        raise RuntimeError(f"Could not confidently align {context} phrase {phrase!r} (best score {score:.2f}, required 0.70). Refusing to render a guessed timeline.")
    return match

def main():
    for p in AUDIO_FILES:
        if not p.is_file():
            raise RuntimeError(f"Missing narration file: {p.relative_to(ROOT)}")
    storyboard = json.loads(STORYBOARD.read_text(encoding="utf-8"))
    cues = json.loads(CUES.read_text(encoding="utf-8"))
    scenes = storyboard.get("scenes", [])
    cue_scenes = cues.get("scenes", [])
    if not scenes or len(scenes) != len(cue_scenes):
        raise RuntimeError(f"Storyboard/cue scene count mismatch: {len(scenes)} storyboard scenes, {len(cue_scenes)} cue scenes.")
    model = WhisperModel("tiny.en", device="cpu", compute_type="int8", cpu_threads=2, num_workers=1)
    words = []
    total = 0.0
    durations = []
    for path in AUDIO_FILES:
        d = duration(path)
        durations.append(d)
        print(f"Transcribing {path.relative_to(ROOT)} ({d:.3f}s), offset {total:.3f}s")
        segments, info = model.transcribe(str(path), language="en", beam_size=5, word_timestamps=True, vad_filter=False, condition_on_previous_text=True)
        count = 0
        for seg in segments:
            count += 1
            if seg.words:
                for word in seg.words:
                    text = word.word.strip()
                    if toks(text):
                        words.append({"text": text, "start": round(total + max(0, float(word.start)), 3), "end": round(total + min(d, float(word.end)), 3)})
            else:
                for token in toks(seg.text):
                    words.append({"text": token, "start": round(total + float(seg.start), 3), "end": round(total + float(seg.end), 3)})
        print(f"  {count} segments; language={info.language}")
        total += d
    words.sort(key=lambda w: w["start"])
    if not words:
        raise RuntimeError("Whisper returned no words.")
    TRANSCRIPT_JSON.parent.mkdir(parents=True, exist_ok=True)
    TRANSCRIPT_JSON.write_text(json.dumps({"generatedBy":"faster-whisper","model":"tiny.en","language":"en","durationSeconds":round(total,3),"audioFiles":[p.relative_to(ROOT / "public").as_posix() for p in AUDIO_FILES],"words":words}, indent=2)+"\n", encoding="utf-8")
    TRANSCRIPT_TEXT.write_text("\n".join(f"[{w['start']:.3f}-{w['end']:.3f}] {w['text']}" for w in words)+"\n", encoding="utf-8")

    # Scene boundaries are anchored to the approved narration, not a weak bag-of-words score.
    boundaries = []
    previous_time = -0.001
    for i, (scene, cue) in enumerate(zip(scenes, cue_scenes)):
        phrase = cue.get("anchor")
        if not phrase:
            raise RuntimeError(f"Missing scene anchor for scene {i+1} ({scene.get('title','untitled')}).")
        match = require_match(words, phrase, previous_time + 0.001, total, f"scene {i+1} start")
        if boundaries and match[2] - boundaries[-1] < 8.0:
            raise RuntimeError(f"Scene {i+1} anchor {phrase!r} is only {match[2]-boundaries[-1]:.1f}s after the previous scene. Check cue order.")
        boundaries.append(match[2])
        previous_time = match[2]
        print(f"Scene {i+1:02d} start {match[2]:.2f}s, anchor score {match[0]:.2f}: {phrase}")

    # Scene 1 begins with the audio. All later starts are phrase-anchored.
    boundaries[0] = 0.0
    boundaries.append(total)
    output = []
    for i, (scene, cue) in enumerate(zip(scenes, cue_scenes)):
        start, end = boundaries[i], boundaries[i+1]
        aligned = {"id":int(scene.get("id",i+1)), "title":scene.get("title",f"Scene {i+1}"), "caption":scene.get("caption",""), "status":scene.get("status",""), "code":scene.get("code",[]), "output":scene.get("output",[]), "prompt":scene.get("prompt"), "errorCode":scene.get("errorCode"), "errorOutput":scene.get("errorOutput"), "errorPrompt":scene.get("errorPrompt"), "correctedCode":scene.get("correctedCode"), "start":round(start,3), "end":round(end,3), "transcriptTopicMatch":1.0}
        # Align code, output, and error/fix transitions to their own spoken cues.
        for cue_key, field_name in [("codeAnchor","codeAt"),("outputAnchor","outputAt"),("errorAnchor","errorAt"),("fixAnchor","fixAt"),("completionAnchor","completionAt")]:
            phrase = cue.get(cue_key)
            if not phrase:
                continue
            match = require_match(words, phrase, start, end, f"scene {i+1} {cue_key}")
            aligned[field_name] = round(match[2],3)
            print(f"  {field_name} {match[2]:.2f}s score {match[0]:.2f}: {phrase}")
        output.append(aligned)
    payload = {"generated":True, "method":"whisper-approved-phrase-anchors", "model":"tiny.en", "durationSeconds":round(total,3), "part2StartSeconds":round(durations[0],3), "audioTracks":[{"src":p.relative_to(ROOT / "public").as_posix(),"start":round(sum(durations[:i]),3)} for i,p in enumerate(AUDIO_FILES)], "scenes":output}
    ALIGNMENT.write_text(json.dumps(payload, indent=2)+"\n", encoding="utf-8")
    print(f"Wrote transcript and {len(output)} phrase-aligned scenes; duration {total:.3f}s")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
