#!/usr/bin/env python3
"""Build a validated, transcript-bearing package for the frame-production tool.

This does not generate frames itself. It creates the explicit input contract that
must be supplied to any external frame maker before it is allowed to create them.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRANSCRIPT = ROOT / "out/lesson-01/transcript.json"
ALIGNMENT = ROOT / "src/generated-alignment.json"
STORYBOARD = ROOT / "docs/LESSON_01_REVISED_STORYBOARD.json"
OUTPUT = ROOT / "out/lesson-01/frame-production-package.json"


def load(path: Path):
    if not path.is_file():
        raise RuntimeError(f"Required pre-frame input is missing: {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc


def main():
    transcript = load(TRANSCRIPT)
    alignment = load(ALIGNMENT)
    storyboard = load(STORYBOARD)
    words = transcript.get("words")
    aligned_scenes = alignment.get("scenes")
    storyboard_scenes = storyboard.get("scenes")

    if not isinstance(words, list) or not words:
        raise RuntimeError("Transcript has no word-level timestamps; refusing to prepare frame inputs.")
    if not isinstance(aligned_scenes, list) or not aligned_scenes:
        raise RuntimeError("Generated alignment has no scenes; refusing to prepare frame inputs.")
    if not isinstance(storyboard_scenes, list) or len(storyboard_scenes) != len(aligned_scenes):
        raise RuntimeError(
            f"Storyboard/alignment mismatch: {len(storyboard_scenes or [])} storyboard scenes, "
            f"{len(aligned_scenes)} aligned scenes."
        )

    scenes = []
    previous_end = 0.0
    for index, (visual, timing) in enumerate(zip(storyboard_scenes, aligned_scenes), start=1):
        start = float(timing.get("start", -1))
        end = float(timing.get("end", -1))
        if start < 0 or end <= start or start < previous_end - 0.01:
            raise RuntimeError(f"Invalid or overlapping timing in scene {index}: start={start}, end={end}.")
        if not visual.get("title") or not visual.get("code") and not visual.get("output"):
            raise RuntimeError(f"Scene {index} is missing a title or visual teaching content.")
        scenes.append({
            "id": timing.get("id", visual.get("id", index)),
            "title": visual.get("title", timing.get("title", f"Scene {index}")),
            "startSeconds": start,
            "endSeconds": end,
            "narrationAnchorSeconds": start,
            "codeAtSeconds": timing.get("codeAt"),
            "outputAtSeconds": timing.get("outputAt"),
            "errorAtSeconds": timing.get("errorAt"),
            "fixAtSeconds": timing.get("fixAt"),
            "teachingVisuals": visual,
        })
        previous_end = end

    package = {
        "schemaVersion": 1,
        "purpose": "Required input package for the frame-making tool; consume this package before creating frames.",
        "lesson": {
            "title": storyboard.get("title"),
            "subtitle": storyboard.get("subtitle"),
            "lessonLabel": storyboard.get("lessonLabel"),
            "sourceStoryboard": "docs/LESSON_01_REVISED_STORYBOARD.json",
        },
        "audio": {
            "files": transcript.get("audioFiles", []),
            "durationSeconds": transcript.get("durationSeconds"),
        },
        "transcript": {
            "generatedBy": transcript.get("generatedBy"),
            "model": transcript.get("model"),
            "language": transcript.get("language"),
            "words": words,
        },
        "scenes": scenes,
        "gate": {
            "transcriptPresent": True,
            "wordTimestampsPresent": True,
            "sceneCountsMatch": True,
            "timingsValidated": True,
            "instruction": "Do not generate frames unless this package and its transcript are loaded by the frame-making tool.",
        },
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(package, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Prepared frame-maker package: {OUTPUT.relative_to(ROOT)}")
    print(f"Transcript words: {len(words)}; scenes: {len(scenes)}; duration: {transcript.get('durationSeconds')}s")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FRAME-PACKAGE ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
