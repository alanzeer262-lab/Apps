# PyLearn Python Basics — Lesson-by-Lesson Script Review

**Status:** Review in progress. Scripts are not approved for narration or rendering merely because files exist.
**Source of truth:** `mohamedalnazeer262-coder/Pylearn-build260`, branch `ccr-c7f6fdd7-xpzi3g`.
**Review rule:** Finish the source comparison, teaching-flow review, code/output checks, and navigation check for one lesson before treating that lesson as ready. Do not bulk-mark lessons complete.

## Review checklist applied to every lesson

1. **Source fidelity:** every required concept is represented; no source requirement is silently dropped; examples stay aligned with the canonical app lesson.
2. **Teaching sequence:** one main idea at a time, appropriate prerequisites, explanations before terminology, prediction pauses before runs, recap matches what was taught.
3. **Code/output correctness:** execute every example; verify exact output, whitespace, types, rounding, and error claims.
4. **Example safety:** examples teach the concept without revealing required exercise answers, hidden tests, or a complete project/capstone solution.
5. **Video usability:** readable phone-sized code, explicit reveal/run/output timing, no duplicate scenes or conflicting versions, narration separated from production notes.
6. **Navigation:** exact lesson/task name and real app path verified; required exercise completion unlocks the next lesson; Practice Drills are optional; project and capstone endings follow their own rules.
7. **Voice and delivery:** Kendrick, ElevenLabs v3, exact approved voice ID verified before narration generation; no guessed ID or substitute voice.
8. **Final watch-through:** inspect the full rendered video at normal speed before approval.

## Lesson 01 — Your First Python Program

**Canonical source:** `content/python-basics/modules/01-first-program.md`
**Script:** `scripts/python-basics/01-your-first-python-program.md`
**Review status:** Lesson and companion script content reviewed; runnable examples executed successfully and the intentionally broken quote was confirmed to raise a SyntaxError. Not approved for video production yet: real app navigation footage and the exact approved voice ID remain unverified, and the rendered video watch-through must happen after production.

### Findings and actions

- **Coverage gap — corrected in the first revision:** the script now includes a source-aligned illustrative profile using name, learning goal, and weekly study hours, with readable f-string output. The learner's turn also asks them to create their own profile. This is a separate example, not the required in-app exercise answer.
- **Pacing / cognitive load — improved, not fully signed off:** scene transitions and visual staging are clearer. The extra completed `double(7)` example was removed so the `pass` section stays focused on recognizing a placeholder rather than adding another function-writing demonstration.
- **Prerequisite framing — corrected:** the script explicitly says learners do not need to design whole functions from scratch yet; they need to recognize a provided starter and understand `return` because the app checks returned values.
- **Repetition — reduced:** the final debugging scene now applies the missing-quote example instead of re-teaching the full routine.
- **Code staging — improved:** scenes 1–6 now include explicit code/output examples and instructions for when to run them. Function definitions, return calls, and the print-only call remain separate so the output sequence is understandable.
- **Source alignment:** the script covers `print`, numeric output, quoted text/strings, matching quotes and a deliberately broken quote example, comments, f-strings, print-versus-return, `None`, `pass`, debugging, and the learner profile task.
- **Navigation remains unverified:** the ending states the required-exercise unlock rule and that Practice Drills are optional. The exact real PyLearn screen/path still needs capture from the app; do not invent or approximate UI in final footage.
- **Voice blocker:** the approved Kendrick voice ID is not recorded in the reviewed repository. Do not generate narration until the exact ID is recovered.

### Code/output QA — executed

The runnable Lesson 1 and P01 companion examples were executed in Python during this review.

- Lesson Scene 1: displays `Hello, I'm Python.`.
- Lesson Scene 2: displays `Hello, I'm Python.` then `5`.
- Lesson Scene 3: both lines display `10`; the values remain different types.
- Lesson Scene 4: the single- and double-quoted examples each display `Hello`. The intentionally malformed `print("Hello)` example raises a `SyntaxError` as expected.
- Lesson Scene 5: displays only `The code still runs.`; the comment is not displayed.
- Lesson Scene 6: displays exactly:
  ```text
  My name is Ada.
  My goal is to learn data analysis.
  I plan to study 6 hours each week.
  ```
- Lesson Scene 7: `add_tip(40)` returns `50`; output is `You pay: 50` and `For a table of two: 100`. The print-only function displays `50`, and the assigned result is `None`.
- P01 Scene 1 displays `Welcome to my study desk!`; Scene 2 displays `10`; Scene 3 displays `Ready to learn`.
- P01 Scene 4 was clarified to show both the broken code and the corrected `print("Hello")` with expected output `Hello`. The broken and corrected versions must be run separately.
- These checks confirm code behavior and expected output for the listed examples. They do not substitute for checking every scene in the final rendered video.

### Remaining production gates

1. Capture and verify the real PyLearn navigation path and required exercise screen; do not invent the UI.
2. Recover and verify the exact approved Kendrick voice ID; use ElevenLabs v3 and do not substitute a voice.
3. Once production is possible, review the complete rendered video at normal speed and check code/output synchronization before marking the video approved.

The source comparison, teaching-flow review, and listed runnable-code QA are complete for this content pass. Video-production approval remains separate from script readiness.

## Guided Practice 01 — First Program

**Script:** `scripts/python-basics/practice/P01-first-program-practice.md`
**Review status:** Content reviewed against the Lesson 1 goals; runnable examples executed; corrected quote example now includes its exact expected output. Not production-approved while the voice ID and real app navigation remain unverified. The companion ending correctly states that it does not complete the required app exercise or unlock the next lesson.

## Lesson 02 — Variables and Data Types

**Canonical source:** `content/python-basics/modules/02-variables-types.md`
**Scripts:** `docs/LESSON_02_NARRATION_SCRIPT.md` and `scripts/python-basics/practice/P02-variables-types-practice.md`
**Review status:** Source comparison and content review completed for both scripts. Runnable examples executed in Python. Two script clarifications committed: the full `type()` output is shown in the lesson script, string repetition is explicitly described as output `2121`, and invalid conversions are labeled as expected `ValueError` examples that must be run separately. The companion now states the expected invalid-input error.

### Findings and code/output QA

- Coverage matches the canonical module: assignment and reassignment, `str`, `int`, `float`, `bool`, `type()`, behavior differences between numbers and strings, conversions, invalid conversion, clear names/snake_case, and prediction before running.
- Executed reassignment examples: `print(name)` outputs `Ada` or `Sam` as shown; assigning `Sam` after `Ada` leaves `Sam` as the final value.
- Executed type example output:
  ```text
  <class 'str'>
  <class 'int'>
  <class 'float'>
  <class 'bool'>
  ```
- Executed `print(21 * 2)` and `print("21" * 2)`: outputs `42` and `2121`.
- Executed `int("21")` followed by adding one: output `22`.
- Executed the prediction example: `25`, `<class 'str'>`, `25`, `<class 'int'>`, `50`, each on its own line.
- Executed the companion's type and conversion examples: output is the expected four type names and `30`.
- Confirmed `int("hello")` and `int("twenty-five")` raise `ValueError`; these are deliberately failing demonstrations and must be run separately from valid examples.
- The learner task does not show a completed solution. The video ending still requires verified real PyLearn navigation footage and the correct required exercise screen.

### Remaining production gates

1. Recover and verify the exact approved Kendrick voice ID; use ElevenLabs v3 and do not substitute a voice.
2. Capture and verify the real PyLearn navigation path and required exercise screen.
3. After production is possible, review the complete rendered video at normal speed and check code/output synchronization before marking it approved.

## Lesson 03 — Numbers and Operators

**Canonical source:** `content/python-basics/modules/03-numbers-operators.md`
**Scripts:** `scripts/python-basics/03-numbers-and-operators.md` and `scripts/python-basics/practice/P03-numbers-practice.md`
**Review status:** The lesson script had duplicated scene sections and two competing final call-to-action endings. It has been consolidated into one coherent ten-scene lesson with one final call to action. The earlier draft also used the required exercise's starting value in an example while later saying not to show that value; examples now use separate values. Runnable examples in the revised lesson and companion were executed in Python.

### Findings and code/output QA

- Coverage matches the canonical module: arithmetic, normal division, floor division, remainder, powers, rounding, operator precedence, parentheses, units, and a mini study report.
- Scene 1 outputs `6.0` for 360 minutes divided by 60.
- Basic operators output `13`, `7`, `30`, and `3.3333333333333335`.
- Floor division and remainder output `3` and `1` for ten divided into groups of three.
- 187 minutes produces `3` complete hours and `7` remaining minutes.
- Normal division versus floor division outputs `3.3333333333333335` and `3`.
- `2 ** 3` outputs `8`; rounding `79.8333333333` to two decimal places outputs `79.83`.
- Precedence examples output `16` without parentheses and `36` with parentheses.
- The 360-minute report outputs `Weekly hours: 6.0` and `Monthly estimate: 24.0`.
- The separate 245-minute example outputs `4.083333333333333`, `4`, `5`, and `16.3`.
- Companion outputs were verified: `4.083333333333333`, then `4` and `5`, and rounded result `4.1`.
- The required exercise's value of 425 minutes is not used in the revised teaching examples; the full exercise answer is not shown.
- Real PyLearn navigation still must be verified before video production.

### Remaining production gates

1. Recover and verify the exact approved Kendrick voice ID; use ElevenLabs v3 and do not substitute a voice.
2. Capture and verify the real PyLearn navigation path and required exercise screen.
3. After production is possible, review the complete rendered video at normal speed and check code/output synchronization before marking it approved.

## Lesson 04 — Strings and f-Strings

**Canonical source:** `content/python-basics/modules/04-strings.md`
**Scripts:** `scripts/python-basics/04-strings-and-fstrings.md` and `scripts/python-basics/practice/P04-strings-practice.md`
**Review status:** Source comparison completed. The main lesson covers strings, zero-based indexing, slicing, whitespace cleanup, capitalization methods, splitting, membership checks, replacement, and f-strings. A source-aligned topic-list example was added to make clear that splitting leaves spaces inside individual items. Runnable examples in the lesson and companion were executed in Python.

### Findings and code/output QA

- Indexing `"Python"` at positions 0 and 1 outputs `P` and `y`.
- Slices output `Py`, `Py`, and `thon`, consistent with the inclusive start and exclusive end.
- For `name = "  ada  "`, outputs are `ada`, `  ADA  `, `  ada  `, and `  Ada  `; only `strip()` removes the outer whitespace. The visual must make those spaces clear.
- Chaining `strip().title()` outputs `Ada`.
- Splitting `"python, pandas, machine learning"` at commas outputs `['python', ' pandas', ' machine learning']`; spaces after commas remain.
- Membership checks output `True` and `False`; lowercasing before the search outputs `True`.
- Replacement outputs `I like Python`; the f-string examples output `Ada scored 92.` and `Next target: 95`.
- The transformation example outputs `DATA, Python`, `data, python`, and `DATA, coding`.
- The added comma-separated list example outputs `['python', ' pandas', ' pandas', ' machine learning']`, confirming that outer stripping does not trim every item.
- Companion outputs were verified: cleaned text `data science, python`; split list `['data science', ' python']`; normalized search outputs `python` and `True`.
- The scripts do not display a completed required exercise solution. Real PyLearn navigation still must be verified before production.

### Remaining production gates

1. Recover and verify the exact approved Kendrick voice ID; use ElevenLabs v3 and do not substitute a voice.
2. Capture and verify the real PyLearn navigation path and required exercise screen.
3. After production is possible, review the complete rendered video at normal speed and check code/output synchronization before marking it approved.

## Lesson 05 — Booleans and Comparisons

**Canonical source:** `content/python-basics/modules/05-booleans.md`
**Scripts:** `scripts/python-basics/05-booleans-and-comparisons.md` and `scripts/python-basics/practice/P05-booleans-practice.md`
**Review status:** Source comparison completed and runnable examples executed in Python. The companion's boundary-testing scene was clarified so the learner sees the exact condition and the expected result for 17, 18, 26, and 27, rather than relying on narration alone.

### Findings and code/output QA

- Coverage matches the canonical source: Boolean values, comparison operators, `=` versus `==`, boundary values, `and`, `or`, `not`, and reading a condition as an English sentence.
- Basic comparison examples output `True` and `False`; the six comparison operators output `True`, `True`, `True`, `False`, `True`, `True`.
- Assignment/comparison example outputs `True` and `False`.
- Boundary check outputs `False` for 69, `True` for 70, and `True` for 71.
- The score and attendance conditions each output `True`, and their combined `and` condition outputs `True`.
- The `or` and `not` examples output `True` and `False`; the readable condition example outputs `True`.
- Companion temperature checks output `True`, `True`, and the combined condition `True`. Boundary results for 17, 18, 26, and 27 are respectively `False`, `True`, `True`, and `False`.
- The examples do not reveal the completed required app exercise. Real PyLearn navigation still must be verified before production.

### Remaining production gates

1. Recover and verify the exact approved Kendrick voice ID; use ElevenLabs v3 and do not substitute a voice.
2. Capture and verify the real PyLearn navigation path and required exercise screen.
3. After production is possible, review the complete rendered video at normal speed and check code/output synchronization before marking it approved.

## Lesson 06 — Lists

**Canonical source:** `content/python-basics/modules/06-lists.md`
**Scripts:** `scripts/python-basics/06-lists.md` and `scripts/python-basics/practice/P06-lists-practice.md`
**Review status:** Source comparison completed and runnable examples executed in Python. Coverage includes list creation, indexing, negative indexing, slicing, appending, replacing items, built-in summary functions, averages, sorting without mutating the original list, membership, and empty-list edge cases.

### Findings and code/output QA

- Creating and printing the score list outputs `[70, 95, 88, 60]`.
- Indexing outputs `70` and `88`; negative index `-1` outputs `60`.
- Slice `scores[1:3]` outputs `[95, 88]`.
- Appending 60 outputs `[70, 95, 88, 60]`; replacing index zero outputs `[75, 95, 88]`.
- List summary outputs `4`, `313`, `60`, and `95`; average is `78.25`.
- `sorted(scores)` outputs `[60, 70, 88, 95]` while the original remains `[70, 95, 88, 60]`.
- Membership checks output `True` and `False`.
- The separate pages example outputs `3`, `45`, `18`, and `True`.
- Companion examples output `4`, `510`, `85`, and `210`; indexing/slicing/appending output `95`, `[85, 210]`, and `[120, 85, 210, 95, 160]`.
- The empty-list division risk is correctly explained; no division-by-zero sample is presented as a successful run.
- The required exercise solution is not displayed. Real PyLearn navigation still must be verified before production.

### Remaining production gates

1. Recover and verify the exact approved Kendrick voice ID; use ElevenLabs v3 and do not substitute a voice.
2. Capture and verify the real PyLearn navigation path and required exercise screen.
3. After production is possible, review the complete rendered video at normal speed and check code/output synchronization before marking it approved.

## Lesson 07 — Conditionals: if / elif / else

**Canonical source:** `content/python-basics/modules/07-conditionals.md`
**Scripts:** `scripts/python-basics/07-conditionals.md` and `scripts/python-basics/practice/P07-conditionals-practice.md`
**Review status:** Compared both scripts with the canonical module and executed all runnable code examples. The companion's boundary-testing scene now includes the exact expected status for values 20, 21, 60, and 61.

### Findings and code/output QA

- The lesson covers the source concepts: if, else, elif, indentation, top-to-bottom branch order, translating rules from plain English, boundary tests, and combining conditions with `and`.
- Lesson example with score 82 outputs `Passed`.
- Lesson if/else example with score 62 outputs `Needs more practice`.
- Ordered grade example with score 84 outputs `B`.
- Combined score/attempts condition outputs `Passed`.
- Companion battery 18 example outputs `Low battery`; battery 55 example outputs `Medium`.
- Companion boundary checks return: 20 → `Low`, 21 → `Medium`, 60 → `Medium`, 61 → `High`.
- The main script preserves the required exercise as learner work and does not show the complete score-classifier solution.
- The source-derived script is content-reviewed, but video production remains unapproved until the voice ID and actual PyLearn navigation are verified and the rendered video receives a full watch-through.

### Remaining production gates

1. Recover and verify the exact approved Kendrick voice ID; use ElevenLabs v3 and do not substitute a voice.
2. Capture and verify the real PyLearn navigation path and required exercise screen.
3. After production is possible, review the complete rendered video at normal speed and check code/output synchronization before marking it approved.

## Lesson 08 — Loops: for and while

**Canonical source:** `content/python-basics/modules/08-loops.md`
**Scripts:** `scripts/python-basics/08-loops.md` and `scripts/python-basics/practice/P08-loops-practice.md`
**Review status:** Compared both scripts with the canonical source and executed all runnable code examples. Coverage includes iteration, accumulators, filtering, unpacking records, while loops, break, and continue. The lesson's final exercise remains learner work; its full solution is not shown.

### Findings and code/output QA

- The name loop outputs Ada, Lin, Sam, and Omar, each on its own line.
- The accumulator example totals the scores to `313`.
- The filtering example outputs `[70, 95, 88]`.
- The record loop outputs `Ada: 88`, `Lin: 72`, and `Sam: 95`.
- The while loop outputs `3`, `2`, and `1`, then terminates.
- The break example outputs `70` and `88`; the loop stops when it reaches 95.
- The continue example outputs `70`, `88`, and `95`, skipping 60.
- Companion examples output the durations `15`, `20`, `10`; total `45`; and filtered list `[20, 35]`.
- The source's next topic is dictionaries, tuples, and sets; the video close does not incorrectly promise another topic beyond the app's lesson flow.
- No required exercise solution is exposed. Real PyLearn navigation and production prerequisites remain unverified.

### Remaining production gates

1. Recover and verify the exact approved Kendrick voice ID; use ElevenLabs v3 and do not substitute a voice.
2. Capture and verify the real PyLearn navigation path and required exercise screen.
3. After production is possible, review the complete rendered video at normal speed and check code/output synchronization before marking it approved.

## Lesson 09 — Dictionaries, Tuples, and Sets

**Canonical source:** `content/python-basics/modules/09-dict-tuple-set.md`
**Scripts:** `scripts/python-basics/09-dictionaries-tuples-sets.md` and `scripts/python-basics/practice/P09-dictionaries-tuples-sets-practice.md`
**Review status:** Compared both scripts with the canonical source and executed all runnable examples. The main lesson covers dictionary lookup/update, tuples and unpacking, looping over records, set uniqueness/membership, frequency counting with `dict.get()`, and choosing the right structure. The required app exercise remains learner work.

### Findings and code/output QA

- Dictionary lookup outputs `Ada` and `88`; updating and adding keys outputs `91` and `beginner`.
- Tuple unpacking outputs `Ada` and `88`.
- The record loop outputs `Ada: 88`, `Lin: 72`, and `Sam: 95`.
- The set example has two unique values and membership returns `True`, producing `2` and `True`.
- Frequency counting outputs `{'A': 3, 'B': 2, 'C': 1}`.
- Companion dictionary outputs `The Little Prince` and `96`; tuple output is `The Hobbit: 310 pages`; set outputs `2` and `True`.
- The lesson's example uses a set literal with a duplicate; Python collapses duplicate values as expected. The narration correctly warns not to rely on set order.
- No completed required-exercise solution is shown. Real PyLearn navigation and production prerequisites remain unverified.

### Remaining production gates

1. Recover and verify the exact approved Kendrick voice ID; use ElevenLabs v3 and do not substitute a voice.
2. Capture and verify the real PyLearn navigation path and required exercise screen.
3. After production is possible, review the complete rendered video at normal speed and check code/output synchronization before marking it approved.

## Lesson 10 — Functions

**Canonical source:** `content/python-basics/modules/10-functions.md`
**Scripts:** `scripts/python-basics/10-functions.md` and `scripts/python-basics/practice/P10-functions-practice.md`
**Review status:** Compared both scripts with the canonical source and executed all runnable examples. Coverage includes defining and calling functions, parameters and arguments, print versus return, single-purpose functions, default parameters, local variables, decomposition, and edge-case testing. The required app exercise and full gradebook solution remain learner work.

### Findings and code/output QA

- The greeting function outputs `Hello, Ada!`; the alternate call outputs `Hello, Lin!`.
- The returning double function outputs `14` and `17` when the returned value is reused.
- The average of `[10, 20, 30]` outputs `20.0`; the local-variable example with `[12, 18, 30]` also outputs `20.0`.
- Default cutoff example outputs `True` for `passed(80)` and `False` for `passed(80, 90)`.
- The script correctly distinguishes the function that prints from the function that returns.
- Companion conversion outputs `1.5`; reused value outputs `Hours: 1.5` and `3.0`; print-only function example outputs `8` followed by `None`.
- Empty-list behavior is explicitly described as an edge case rather than incorrectly presented as a successful average.
- No completed required-exercise solution is shown. Real PyLearn navigation and production prerequisites remain unverified.

### Remaining production gates

1. Recover and verify the exact approved Kendrick voice ID; use ElevenLabs v3 and do not substitute a voice.
2. Capture and verify the real PyLearn navigation path and required exercise screen.
3. After production is possible, review the complete rendered video at normal speed and check code/output synchronization before marking it approved.

## Lesson 11 — Comprehensions, Imports, and Safe Conversion

**Canonical source:** `content/python-basics/modules/11-comprehensions-imports.md`
**Scripts:** `scripts/python-basics/11-comprehensions-imports-safe-conversion.md` and `scripts/python-basics/practice/P11-comprehensions-safe-conversion-practice.md`
**Review status:** Compared both scripts with the canonical source and executed all runnable examples. The lesson's invalid conversion example is now explicitly labeled as an expected `ValueError` and must be run separately from the successful and safe-conversion examples.

### Findings and code/output QA

- The raw input list outputs `['88', '72', 'oops', '95']`.
- Loop and comprehension versions both output `[140, 160, 180]`.
- The filtering comprehension outputs `[70, 84, 92]`.
- `math.sqrt(25)` outputs `5.0`; `statistics.mean([70, 80, 90])` outputs `80`.
- The None example outputs `None` and `True`; it correctly distinguishes absence from zero, an empty string, and False.
- `int("88")` outputs `88`; `int("oops")` raises `ValueError` as expected.
- The safe-conversion example catches `ValueError`, then outputs `None` and `True`.
- Companion comprehension outputs `[4, 8, 12]`; companion mean outputs `20`; `safe_int("42")` and `safe_int("oops")` output `42` and `None`.
- The scripts do not complete the required safe-conversion exercise or expose its full solution. Real PyLearn navigation and production prerequisites remain unverified.

### Remaining production gates

1. Recover and verify the exact approved Kendrick voice ID; use ElevenLabs v3 and do not substitute a voice.
2. Capture and verify the real PyLearn navigation path and required exercise screen.
3. After production is possible, review the complete rendered video at normal speed and check code/output synchronization before marking it approved.

## Lesson 12 — Project 1: My Learning Report

**Canonical source:** `content/python-basics/modules/12-build-personal-report.md`
**Scripts:** `scripts/python-basics/12-my-learning-report.md` and `scripts/python-basics/practice/P12-learning-report-practice.md`
**Review status:** Compared both scripts with the canonical project brief and executed the demonstration code. The required function `build_learning_report(name, goal, weekly_hours, active)` is not implemented or revealed in the video script. The companion uses a separate reading-report example.

### Findings and code/output QA

- The main script preserves the source requirements: four-line report with name, goal, weekly study hours, and active/inactive status; the function must return the report, not print it.
- The main script's separate Boolean-status demonstration outputs `Open`; the separate greeting function outputs `Welcome, Lin!`.
- The required output is shown only as an unfilled field template, not as a completed solution.
- The companion's reading-report function outputs:
  ```text
  Reader: Mia
  Goal: Read more science
  Books this month: 3
  ```
- The companion uses different fields and a fictional reading example, so it demonstrates multi-line returned strings without solving the required learner-report task.
- The source asks learners to test a normal learner, zero study hours, and an inactive learner; the main script discusses those cases without revealing a completed answer.
- Real PyLearn project-task navigation and production prerequisites remain unverified.

### Remaining production gates

1. Recover and verify the exact approved Kendrick voice ID; use ElevenLabs v3 and do not substitute a voice.
2. Capture and verify the real PyLearn navigation path and required project task screen.
3. After production is possible, review the complete rendered video at normal speed and check code/output synchronization before marking it approved.

## Lesson 13 — Project 2: Study Time Calculator

**Canonical source:** `content/python-basics/modules/13-build-study-calculator.md`
**Scripts:** `scripts/python-basics/13-study-time-calculator.md` and `scripts/python-basics/practice/P13-study-time-practice.md`
**Review status:** Compared both scripts with the canonical project brief and executed all demonstration examples. The required `study_time_report(total_minutes, sessions)` solution is not shown.

### Findings and code/output QA

- The canonical brief requires total minutes, full hours, remaining minutes, average session length, deliberate use of division/floor division/modulo/rounding, and the exact zero-session message: `No study sessions recorded.`
- The main example with 245 minutes outputs decimal hours `4.083333333333333`, rounded display `4.1`, full hours `4`, and leftover minutes `5`.
- The separate average example (150 minutes over 5 sessions) outputs `30.0`.
- The companion example with 95 minutes outputs `1.5833333333333333`, `1`, and `35`; the average example outputs `20.0`.
- The script correctly discusses zero sessions and tells learners to implement the specified message, without giving the complete required function.
- The required project tests (360 minutes over 6 sessions, 65 minutes over 2 sessions, and zero sessions) are not presented as solved outputs.
- Real PyLearn project-task navigation and production prerequisites remain unverified.

### Remaining production gates

1. Recover and verify the exact approved Kendrick voice ID; use ElevenLabs v3 and do not substitute a voice.
2. Capture and verify the real PyLearn navigation path and required project task screen.
3. After production is possible, review the complete rendered video at normal speed and check code/output synchronization before marking it approved.

## Lesson 14 — Project 3: Clean My Learning Topics

**Canonical source:** `content/python-basics/modules/14-build-topic-cleaner.md`
**Scripts:** `scripts/python-basics/14-clean-my-learning-topics.md` and `scripts/python-basics/practice/P14-clean-topics-practice.md`
**Review status:** Compared both scripts with the canonical project brief and executed the demonstration examples. The main script's raw-text example now uses `repr()` so leading and trailing spaces are visibly verifiable. The full `clean_topics` implementation is not shown.

### Findings and code/output QA

- The source rules are preserved: split on commas, remove surrounding whitespace, normalize capitalization, ignore empty pieces, and search without case sensitivity.
- The raw-text example outputs `'  data, Python, data  '`, making the spaces visible.
- Splitting outputs `['data', ' Python', ' data']`; spaces inside individual pieces remain until they are cleaned.
- Cleaning and lowercasing outputs `python`.
- Repeated separators output `['python', '', 'pandas']`, correctly demonstrating the empty piece that the project must ignore.
- Case-insensitive comparison outputs `True`.
- Companion hobby example outputs `['hiking', ' cooking', ' hiking']`; normalizing one hobby outputs `cooking`; normalized membership outputs `True`.
- The companion uses hobbies rather than the required project data and does not reveal the required function solution.
- Real PyLearn project-task navigation and production prerequisites remain unverified.

### Remaining production gates

1. Recover and verify the exact approved Kendrick voice ID; use ElevenLabs v3 and do not substitute a voice.
2. Capture and verify the real PyLearn navigation path and required project task screen.
3. After production is possible, review the complete rendered video at normal speed and check code/output synchronization before marking it approved.

## Lesson 15 — Project 4: Score Summary

**Canonical source:** `content/python-basics/modules/15-build-score-summary.md`
**Scripts:** `scripts/python-basics/15-score-summary.md` and `scripts/python-basics/practice/P15-score-summary-practice.md`
**Review status:** Compared both scripts with the canonical project brief and executed all demonstration examples. The required `summarize_scores` implementation and its complete returned dictionary remain learner work.

### Findings and code/output QA

- The source requires a returned dictionary with count, average, highest, lowest, and passed; the empty list must return a deliberate result rather than crash.
- The main independent example outputs count `4`, average `78.75`, highest `91`, and lowest `62`.
- The threshold example outputs `True` for score 70 and threshold 70, correctly including the boundary.
- The companion ratings example outputs count `4`, average `3.5`, highest `5`, and lowest `2`; its threshold example outputs `True`.
- The scripts explain empty-list handling without inventing a specific empty-result structure that the canonical brief does not define.
- Required app test values and the completed solution are not shown as solved output. Real PyLearn project-task navigation and production prerequisites remain unverified.

### Remaining production gates

1. Recover and verify the exact approved Kendrick voice ID; use ElevenLabs v3 and do not substitute a voice.
2. Capture and verify the real PyLearn navigation path and required project task screen.
3. After production is possible, review the complete rendered video at normal speed and check code/output synchronization before marking it approved.

## Lesson 16 — Project 5: Multi-Record Progress Analyzer

**Canonical source:** `content/python-basics/modules/16-build-progress-analyzer.md`
**Scripts:** `scripts/python-basics/16-multi-record-progress-analyzer.md` and `scripts/python-basics/practice/P16-progress-analyzer-practice.md`
**Review status:** Compared both scripts with the canonical project brief and executed all demonstration examples. The required `analyze_records` function and complete returned summary remain learner work.

### Findings and code/output QA

- The source requires count, average, top scorer, passed, and needs_support; the learner lists must preserve input order and empty records must be handled.
- The main record loop outputs `Mia: 81`, `Noah: 67`, and `Iris: 93`.
- The separate passing-rule example outputs `Mia passed` and `Iris passed`, matching the threshold of 70.
- Companion accumulator outputs `7`; max example outputs `3`.
- The main script explains empty input and preserving order without presenting the full analyzer solution or the canonical required records as a completed result.
- Real PyLearn project-task navigation and production prerequisites remain unverified.

### Remaining production gates

1. Recover and verify the exact approved Kendrick voice ID; use ElevenLabs v3 and do not substitute a voice.
2. Capture and verify the real PyLearn navigation path and required project task screen.
3. After production is possible, review the complete rendered video at normal speed and check code/output synchronization before marking it approved.

## Lesson 17 — Project 6: Grade Distribution

**Canonical source:** `content/python-basics/17-build-grade-distribution.md`
**Scripts:** `scripts/python-basics/17-grade-distribution.md` and `scripts/python-basics/practice/P17-category-counts-practice.md`
**Review status:** Compared both scripts with the canonical project brief and executed all demonstration examples. The required two-function solution remains learner work.

### Findings and code/output QA

- The source's category boundaries are preserved: 90+ → A, 80–89 → B, 70–79 → C, 60–69 → D, below 60 → F.
- The independent score example (86) outputs `B`.
- The separate frequency-count example outputs `{'A': 2, 'B': 2, 'C': 1}`.
- Companion speed example outputs `Medium`; its category frequency table outputs `{'Fast': 2, 'Medium': 2, 'Slow': 1}`.
- The main script describes testing boundary pairs and checking that category counts sum to the number of inputs, without revealing the source's required example distribution.
- The required grade-conversion and grade-counting functions are not implemented in the script. Real PyLearn project-task navigation and production prerequisites remain unverified.

### Remaining production gates

1. Recover and verify the exact approved Kendrick voice ID; use ElevenLabs v3 and do not substitute a voice.
2. Capture and verify the real PyLearn navigation path and required project task screen.
3. After production is possible, review the complete rendered video at normal speed and check code/output synchronization before marking it approved.

## Lesson 18 — Project 7: Reusable Analysis Toolkit

**Canonical source:** `content/python-basics/modules/18-build-toolkit.md`
**Scripts:** `scripts/python-basics/18-reusable-analysis-toolkit.md` and `scripts/python-basics/practice/P18-reusable-functions-practice.md`
**Review status:** Compared both scripts with the canonical project brief and executed all runnable examples. The required `average_score` and `top_scorer` functions remain learner work, including their deliberate empty-case rules.

### Findings and code/output QA

- The main independent helper `total_points([12, 18, 20])` outputs `50`.
- Reusing `total_points([5, 10, 15])` and dividing by three outputs `10.0`.
- Companion helper `total_pages([10, 20, 30])` outputs `60`; reuse with two inputs outputs `20` and `40`.
- The scripts correctly distinguish the two required functions and emphasize clear inputs, useful return values, and explicit empty-case behavior.
- The lesson does not invent the project's exact empty-case outputs or reveal the full required functions. Real PyLearn project-task navigation and production prerequisites remain unverified.

### Remaining production gates

1. Recover and verify the exact approved Kendrick voice ID; use ElevenLabs v3 and do not substitute a voice.
2. Capture and verify the real PyLearn navigation path and required project task screen.
3. After production is possible, review the complete rendered video at normal speed and check code/output synchronization before marking it approved.

## Lesson 19 — Project 8: Handle Imperfect Scores

**Canonical source:** `content/python-basics/modules/19-build-messy-input.md`
**Scripts:** `scripts/python-basics/19-handle-imperfect-scores.md` and `scripts/python-basics/practice/P19-imperfect-input-practice.md`
**Review status:** Compared both scripts with the canonical project brief and executed all runnable examples. The complete `clean_score_records` implementation and required dataset output remain learner work.

### Findings and code/output QA

- The source requires valid records to become numeric tuples and invalid records to retain the name plus a reason such as invalid score or empty score.
- The valid conversion example outputs `88` and `<class 'int'>`.
- Converting `"oops"` directly to an integer raises `ValueError`; the safe example catches it and outputs `True` for the None check.
- The companion quantity example outputs `15`; its invalid-text example outputs `True` after safely representing the value as None.
- The main script correctly distinguishes empty text from invalid non-empty text and says invalid scores must not be silently changed to zero.
- The invalid conversion scene narrates the expected ValueError, but should be made more explicit in the script markup before production by labeling it as an intentional failing example and stating the expected error directly.
- Real PyLearn project-task navigation and production prerequisites remain unverified.

### Remaining content and production gates

1. Clarify the invalid-conversion scene with an explicit “expected ValueError; run separately” label and expected-error note.
2. Recover and verify the exact approved Kendrick voice ID; use ElevenLabs v3 and do not substitute a voice.
3. Capture and verify the real PyLearn navigation path and required project task screen.
4. After production is possible, review the complete rendered video at normal speed and check code/output synchronization before marking it approved.

## Lesson 20 — Mini Gradebook Capstone

Not yet reviewed in this pass. Its source and companion will be checked individually before the script is approved. File existence or a link in the index is not evidence of QA completion.
