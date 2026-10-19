# PyLearn Video Studio — Master File Map

## First action for new recordings
**Unclassified/new MP3s:** `incoming/audio/`
Upload original files here without renaming. The assistant identifies their spoken content before assigning permanent destinations.

## Permanent track locations
- Track 1 — Python Basics: `tracks/track-01-python-basics/`
- Track 2 — Python Foundations: `tracks/track-02-python-foundations/`
- Each unit has separate `lesson/` and `practice/` folders. Audio goes in the corresponding folder as `audio/lesson.mp3` or `audio/practice.mp3`.
- Narration scripts go in the matching folder as `script.md`.
- Transcript and word timing artifacts go in the matching folder's `transcript/`.
- Lesson-specific visual assets go in the matching folder's `assets/`.
- Final approved rendered videos remain in `public/videos/final/`.
- Test renders remain in `public/videos/previews/`.
- Shared rendering/alignment code remains in `scripts/`.
- Project status, decisions and process documentation live in `docs/`.

## Existing production compatibility
The current Lesson 1 workflow uses `public/audio/lesson-01/part-01.mp3` and `public/audio/lesson-01/part-02.mp3`. Preserve these paths until the renderer and GitHub Actions workflow are deliberately migrated and tested. Do not assume the new track folders are wired into rendering yet.

## Unit inventory
### Track 1 — Python Basics
1. `first-python-program` — First Program
2. `variables-and-types` — Variables & Types
3. `numbers-and-operators` — Numbers & Operators
4. `strings` — Strings
5. `booleans` — Booleans
6. `lists` — Lists
7. `conditionals` — Conditionals
8. `loops` — Loops
9. `dictionaries-tuples-sets` — Dictionaries, Tuples & Sets
10. `functions` — Functions
11. `comprehensions-and-imports` — Comprehensions & Imports
12. `mini-gradebook-capstone` — Mini Gradebook Capstone

### Track 2 — Python Foundations
1. `debugging-smaller-questions` — Debugging: Ask Smaller Questions
2. `files-and-csv-records` — Files and CSV Records
3. `organize-a-growing-program` — Organize a Growing Program
4. `validation-and-testing` — Validation and Testing
5. `think-in-tables-before-pandas` — Think in Tables Before pandas
6. `raw-records-to-reliable-report` — From Raw Records to a Reliable Report
7. `build-load-scores-csv` — Build: Load a Scores CSV
8. `build-validate-intake` — Build: Validate Intake
9. `build-summary-report` — Build: Summary Report
10. `build-run-the-pipeline` — Build: Run the Pipeline
11. `learning-analytics-toolkit-capstone` — Learning Analytics Toolkit Capstone

## Naming conventions
- Use lowercase kebab-case for unit folders and descriptive source files.
- Preserve original generated audio filenames in `incoming/audio/` until the content has been identified.
- Permanent lesson audio filename: `lesson.mp3`.
- Permanent practice audio filename: `practice.mp3`.
- Never identify or assign audio by duration alone.
