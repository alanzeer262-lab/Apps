# PyLearn Python Basics — Runway Production Pack (Master Brief)

> **Full script index:** [RUNWAY_READY_SCRIPT_INDEX.md](RUNWAY_READY_SCRIPT_INDEX.md) — 20 complete lesson-video scripts plus 20 separate guided-practice companion scripts.
>
> **Voice-ID gate:** The exact approved Kendrick voice ID is not present in the repository files reviewed. Verify it from the original Runway setup before generating any narration. Do not guess or substitute a voice.


Status: **Script set authored — 20 lesson scripts and 20 guided-practice scripts are indexed. Production is not yet approved: the exact Kendrick voice ID is still missing, code/output QA and real navigation-footage verification remain required. Do not spend narration-generation credits until the voice ID is verified.**

Canonical curriculum: `mohamedalnazeer262-coder/Pylearn-build260`, branch `ccr-c7f6fdd7-xpzi3g`.
Video project: `mohamedalnazeer262-coder/pylearn-video-studio.`, branch `main`.
The app track has 20 modules: 11 concept lessons, 8 project lessons, and 1 capstone.

## Non-negotiable production rules

- **Voice:** ElevenLabs v3, voice **Kendrick**, using the exact previously approved voice ID. Do not substitute a voice or guess the ID. If Runway cannot access it, stop and report that limitation.
- **Do not generate a new narration voice in Runway** when approved narration audio is provided. Use the supplied narration file as the timing master.
- **Format:** 16:9 landscape, 1920×1080 target, 30 fps, clean educational explainer, readable code, restrained motion, no stock footage montage, no fake app UI.
- **Code accuracy:** Render code as exact typeset overlays or screen recordings, not AI-generated text. Verify every character, quote, indent, operator, output, and capitalization. Do not ask the video model to invent code text.
- **Visual identity:** Calm modern learning product; dark editor surface, high-contrast syntax, simple warm accent, consistent typography. Keep code large enough to read on a phone.
- **Audio:** Voice remains clear and forward. Music is optional and very quiet; no music under important code explanation if it reduces clarity.
- **Teaching:** Show one idea at a time. Use a visible cursor/highlight, slow purposeful edits, and pauses for prediction. Never rush through code.
- **Truthfulness:** Do not show PyLearn screens unless a real screenshot/screen recording is supplied. Otherwise use a neutral code-editor mockup labelled as an illustrative example.
- **No answer leakage:** Required app exercise answers, full project solutions, test cases, or capstone solutions must not appear in lesson or guided-practice videos.
- **Video-to-app flow:** Lesson video teaches. Separate guided-practice video demonstrates a fresh analogous example. Learner then opens PyLearn and completes the actual required coding exercise. Optional Practice Drills are optional and never a progression gate. Only passing the required exercise unlocks the next lesson.
- **YouTube CTA:** Tell the viewer to open PyLearn and locate the exact lesson/task. The video does not count as completing the app exercise.

## Production workflow

1. Approve the narration text and example code first.
2. Record/export narration with the locked Kendrick voice; preserve the original approved audio.
3. Create scenes using the scene plans below. Use exact code overlays or screen capture.
4. Align each scene to the narration waveform; never speed up speech to fit visuals.
5. Add captions from the approved transcript; check Python symbols and punctuation manually.
6. Export a low-cost review preview first. Do not create final high-resolution renders until text, timing, and CTA are checked.
7. QA on a phone-sized preview: readable code, safe margins, no clipped captions, no hallucinated text, no audio gaps.
8. Store final video, narration, subtitle file, and QA checklist in the video repository.

## Shared Runway instruction (paste before each scene plan)

Create a polished, calm Python-learning explainer in 16:9 landscape. Use restrained camera movement, clean cuts, and readable composition. Treat all supplied code and text as locked source material: do not rewrite, hallucinate, decorate, or alter it. Use the provided narration audio as the timing master; do not synthesize a replacement voice. Keep every code sample static and legible long enough to read. Use no unverified PyLearn interface, no extra claims, no answer key, and no distracting stock montage. If a scene needs exact code, use a screen recording or typeset overlay rather than generated lettering.

## Video inventory

Each module requires **two videos**:
- **Lesson video (L01–L20):** full teaching/project orientation.
- **Guided practice video (P01–P20):** short companion using original, analogous examples. It must not duplicate or reveal the required app exercise solution.

The concept lessons are 1–11. Project videos 12–19 orient and teach a representative technique but leave meaningful implementation to the learner. The capstone video 20 explains milestones and workflow without giving completed answers.

---

## Lesson video scene plans

### L01 — Your first Python program
**Learning goals:** `print()`, text vs numeric output, comments, f-strings as introduced in the canonical lesson, reading syntax errors calmly, and distinguishing displayed output from returned values only if the approved narration covers it.
**Scenes:**
1. Hook: a blank editor, question “How do you make a computer speak?”
2. Type and run `print("Hello, I'm Python.")`; show exact output.
3. Two-line output and `print(2 + 3)`; reveal output after a short prediction pause.
4. Contrast `print(10)` and `print("10")`; label “number” vs “text” without teaching all types early.
5. Show matching quotes and a deliberately broken quote; display a simple SyntaxError, then repair it.
6. Show a comment beginning with `#`; code still runs.
7. Use the approved f-string example only if it remains in the final lesson script; highlight braces around the variable.
8. Recap the write → run → observe loop; CTA to PyLearn Lesson 1 required coding exercise.
**Avoid:** teaching functions/return/pass in depth; revealing either required exercise answer.

### L02 — Variables and data types
**Learning goals:** assignment, variable labels, `str`, `int`, `float`, `bool`, `type()`, conversions, snake_case, and invalid conversion behavior.
**Scenes:** Hook about remembering learner details; assign and reassign `name`; show four data types; use `type()`; contrast `21 * 2` with `"21" * 2`; convert `"21"` with `int()`; show `float()` and `str()`; show `int("hello")` failing and explain that input must be valid; finish with clear variable naming and CTA to Lesson 2 exercise.
**Avoid:** presenting invalid conversion as a mysterious crash; showing app exercise answers.

### L03 — Numbers and operators
**Learning goals:** arithmetic, `/`, `//`, `%`, `**`, precedence, parentheses, `round()`, and unit reasoning.
**Scenes:** study minutes hook; basic arithmetic; compare `10 / 3` and `10 // 3`; pair `//` and `%` to split minutes into hours/remainder; show `2 ** 3`; round a decimal; compare `10 + 2 * 3` with `(10 + 2) * 3`; end with “check the units” and app CTA.

### L04 — Strings and f-strings
**Learning goals:** character sequence, zero-based indexing, slicing, common string methods, `split()`, membership, replacement, f-strings.
**Scenes:** messy topic text hook; display characters and index positions; slice with included start/excluded end; clean whitespace with `strip()`, then `title()`; split a comma-separated string; show membership and replacement with an unrelated sample; use an f-string to compose a message; CTA to Lesson 4 exercise.
**Avoid:** using required exercise input/output.

### L05 — Booleans and comparisons
**Learning goals:** `True`/`False`, comparisons, `==` vs `=`, `>=`/`<=`, `and`/`or`/`not`, boundary testing.
**Scenes:** yes/no decision hook; animate comparison expressions into boolean results; highlight assignment vs equality; test 69, 70, 71 against a passing threshold; show a compound condition and explain each part; CTA.

### L06 — Lists
**Learning goals:** list creation, indexing, negative indexing, slicing, item updates, `append()`, `len()`, `sum()`, `min()`, `max()`, `sorted()`, membership.
**Scenes:** why collections matter; introduce a fresh list; index and negative index; slice while noting end is excluded; append and replace one item; display useful built-ins; show membership check; recap ordered, mutable collection; CTA.

### L07 — Conditionals
**Learning goals:** `if`, `elif`, `else`, indentation, branching order, boundary-aware rules.
**Scenes:** decision tree hook; show one `if`; highlight four-space indentation; add `else`; introduce multiple ranges with `elif`; trace one sample value from top to bottom; show a common ordering mistake then fix it; CTA.

### L08 — Loops
**Learning goals:** `for`, `while`, iteration, accumulators, filtering, `break`, `continue` where included in approved script.
**Scenes:** list of names too long to handle manually; loop over items; trace one iteration at a time; sum scores using an accumulator; filter scores into a new list; explain loop progress and avoiding an infinite `while`; show break/continue only if included in the final narration; CTA.

### L09 — Dictionaries, tuples, and sets
**Learning goals:** key/value lookup and updates, tuple records/unpacking, sets and uniqueness, membership/frequency counting if included.
**Scenes:** compare collection needs; dictionary with learner fields and key lookup; update/add a field; tuple record and unpacking; loop over records; set removes duplicates; use a set membership example; recap which structure fits which job; CTA.

### L10 — Functions
**Learning goals:** defining and calling functions, parameters, arguments, return values, local reusable logic as covered by canonical module.
**Scenes:** repeated calculation hook; define a tiny function unrelated to app task; call it with different arguments; trace parameter → function body → return value; contrast `print()` with `return`; explain one focused function is easier to test; CTA. Use only syntax supported by the approved script.

### L11 — Comprehensions, imports, and safe conversion
**Learning goals:** comprehension as compact transformation/filtering, importing standard-library tools, safe conversion patterns from canonical lesson.
**Scenes:** start with a small loop; show equivalent comprehension and explain each part; filter a fresh list; import a standard-library module only if specified in source; show safe input conversion using a try/except pattern only if present in approved curriculum; emphasize readable code over clever one-liners; CTA.

### L12 — Build a personal report
**Goal:** introduce the personal-report project and its requirements without showing the completed solution.
**Scenes:** present a fictional study profile and report goal; identify inputs, calculations, and output sections; demonstrate one small independent formatting/calculation example; show a checklist of requirements, not completed report; remind learner to implement in PyLearn and run tests.

### L13 — Build a study calculator
**Goal:** orient the study calculator project.
**Scenes:** show a fictional weekly study plan; identify variables, arithmetic, and output; demonstrate one unrelated minutes-to-hours example; present the project requirements as a checklist; do not show complete calculator logic or expected final answer; CTA to project task.

### L14 — Build a topic cleaner
**Goal:** introduce cleaning and organizing topic text.
**Scenes:** show messy text with extra spaces and inconsistent capitalization; demonstrate `strip()` and `split()` on a different string; show transformation stages visually; keep required project input and full output off screen; CTA.

### L15 — Build a score summary
**Goal:** orient score aggregation and summary.
**Scenes:** display a tiny fictional list not matching exercise data; explain count, total, average, min/max as applicable to source; demonstrate one simple built-in; leave project calculations and output to learner; CTA.

### L16 — Build a progress analyzer
**Goal:** explain how to derive progress indicators from records.
**Scenes:** show fictional weekly progress data; identify what should be counted or compared; demonstrate a small independent accumulator/filter example; avoid the complete project algorithm; CTA.

### L17 — Build grade distribution
**Goal:** understand categories and distribution.
**Scenes:** use an unrelated mini data set; explain that each score belongs in a band/category according to clear rules; demonstrate a single category decision without completing all bands; visualize categories as simple bars; CTA.

### L18 — Build a toolkit
**Goal:** combine small reusable helpers into a toolkit.
**Scenes:** explain why related small functions are useful; demonstrate one simple unrelated helper function; show how functions can be called in sequence; provide an architecture overview, not full implementation; CTA.

### L19 — Build messy input
**Goal:** handle messy or invalid input robustly using techniques already taught.
**Scenes:** show blank, padded, and malformed sample text; explain trim → validate/convert → decide what to do; demonstrate a safe small example not matching task data; distinguish expected invalid input from a bug; no full solution; CTA.

### L20 — Mini Gradebook capstone
**Goal:** prepare learner for a multi-milestone project without solving it.
**Scenes:** introduce the fictional gradebook and record concept; preview the five milestone objectives using short labels taken from the current capstone specification; show how to approach one milestone at a time; explain run/check/fix/retry; do not show the full `count_passing(records, threshold)` implementation or completed milestone outputs; direct learner to open Mini Gradebook Capstone and begin Milestone 1.

---

## Guided-practice companion videos (P01–P20)

Each companion is a separate short video (target 2–4 minutes, depending on topic). It must use an **original example created for the video**, different from the required app exercise. Teach the reasoning, predict the result, reveal it, and ask the learner to pause and try a variation. End by directing the learner to the actual required task in PyLearn. Never claim that completing the companion video unlocks anything.

- **P01 — print/comments/errors:** use a “Welcome to my study desk” message, a small arithmetic print, one comment, and repair a mismatched quote. Then open Lesson 1 in PyLearn.
- **P02 — variables/types:** use `course = "Python"`, `minutes = 25`, `rating = 4.5`, `is_ready = True`; inspect types and convert a numeric string. Then open Lesson 2.
- **P03 — numbers:** convert a fictional 245 minutes into hours/remainder; compare normal and floor division; ask learner to predict before revealing. Then open Lesson 3.
- **P04 — strings:** clean `"  data science, python  "`, split on comma, inspect first characters, and build a friendly f-string. Then open Lesson 4.
- **P05 — booleans:** decide whether a fictional temperature is within a range; compare `==`, `>=`, `and`, and `or`. Then open Lesson 5.
- **P06 — lists:** use a fresh list of book page counts; access last item, slice, append, and compute total. Then open Lesson 6.
- **P07 — conditionals:** classify fictional battery levels as low/medium/high; trace branches and indentation. Then open Lesson 7.
- **P08 — loops:** iterate over a fresh list of task durations and calculate a total; optionally filter durations over a threshold. Then open Lesson 8.
- **P09 — dictionaries/tuples/sets:** represent a fictional book as a dictionary, unpack a tuple, and deduplicate tags with a set. Then open Lesson 9.
- **P10 — functions:** create `minutes_to_hours(minutes)` with a simple return; call it twice and distinguish return from print. Then open Lesson 10.
- **P11 — comprehensions/imports/safe conversion:** transform a fresh list of words; show a readable comprehension; demonstrate a small safe conversion only if it matches taught syntax. Then open Lesson 11.
- **P12 — personal report:** use a separate fictional reading habit and outline a report with one computed field; leave the app report implementation to the learner.
- **P13 — study calculator:** use a different short study-time example to calculate a total; do not reproduce project requirements verbatim or final output.
- **P14 — topic cleaner:** clean a fresh string of hobbies/tags, showing each transformation step.
- **P15 — score summary:** use a different tiny set of fictional scores to explain average and range without matching task data.
- **P16 — progress analyzer:** use fictional daily habit counts and calculate one simple trend/total.
- **P17 — grade distribution:** classify a tiny unrelated set of example values; demonstrate one category and ask learner to classify the rest.
- **P18 — toolkit:** build one tiny unrelated helper function and explain how multiple helpers can work together.
- **P19 — messy input:** use a fictional quantity string with spaces and a clearly invalid example; show a safe handling approach only if already taught.
- **P20 — capstone orientation practice:** use a tiny unrelated two-record example to practice reading record fields and stating a passing rule; do not implement the capstone function or any milestone solution. End with “Open Mini Gradebook Capstone and start Milestone 1.”

## Standard closing script

For concept lessons 1–11:
“Now it’s your turn to write code yourself. Open PyLearn and go to Lesson [number], then complete its required coding exercise. If you’re watching on YouTube, open PyLearn and find this lesson there. Run your code, read the feedback, and fix mistakes as needed. Practice Drills are optional. Passing the required exercise is what unlocks the next lesson. Pause this video and start coding.”

For project lessons 12–19:
“Now open PyLearn and find the [project title] task. Build it yourself and run the tests. This video has shown the ideas, not the finished solution. Practice Drills, if shown, are optional; complete and pass the required project exercise to unlock the next lesson. Pause the video and start building.”

For capstone:
“Open PyLearn and enter Mini Gradebook Capstone. Start with Milestone 1, submit your work, read the feedback, and fix what you need to fix before moving on. Work through the milestones one at a time. The solution is yours to build.”

## Final quality checklist

- [ ] Approved narration audio is used; exact Kendrick voice ID not changed.
- [ ] Narration matches visible scene; no scene races ahead.
- [ ] Every code sample was executed in Python and output verified.
- [ ] No required app exercise answer, hidden test, or full project/capstone solution is exposed.
- [ ] All on-screen code is readable on a phone.
- [ ] Captions, quotes, underscores, indentation, and operators are manually checked.
- [ ] CTA identifies the right PyLearn lesson/task and explains the required exercise gate.
- [ ] Practice video uses an original analogous example, not the required exercise.
- [ ] Final export has no unverified app UI or AI-generated text artifacts.
