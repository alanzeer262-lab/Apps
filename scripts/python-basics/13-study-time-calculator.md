# PyLearn Video 13 — Project 2: Study Time Calculator

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generating audio.
> - No guessed ID, substitution, or preset. Use the same approved voice identity throughout.
> - Speak narration only; do not read headings or bracketed directions aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/13-build-study-calculator.md`, branch `ccr-c7f6fdd7-xpzi3g`.  
**Target runtime:** Approximately 5–7 minutes.  
**Project-video rule:** Explain the approach with an original example; do not show the complete required function or its finished solution.

## Scene 1 — Ask the right questions about time

**Visual:** Show a fictional total of 245 study minutes. Introduce the questions: decimal hours, complete hours, leftover minutes, and average session length. Do not use the project's required test values.

**Narration:**

Welcome back. In this project, you're going to build a study-time calculator.

A total number of minutes can answer several different questions. How many hours is that as a decimal? How many complete hours are there? How many minutes remain after the complete hours? And if the study time was divided into sessions, what was the average session length?

Before writing code, be clear about each question. The same input can be represented in different useful ways, and the operator you choose should match the question you're asking.

## Scene 2 — Convert minutes to hours

**Visual:** Reveal the variables and normal division. Run only after the narration asks the learner to predict.

**Code**
```python
study_minutes = 245
hours = study_minutes / 60
print(hours)
```

**Expected output**
```text
4.083333333333333
```

**Narration:**

There are sixty minutes in an hour, so normal division converts minutes to decimal hours. Two hundred and forty-five divided by sixty gives a little more than four hours.

The result has many decimal places. For a report, you may want to round the result to a chosen number of decimal places.

**Code**
```python
print(round(hours, 1))
```

**Expected output**
```text
4.1
```

**Narration:**

Here, round keeps one decimal place. The unrounded value remains stored in hours; this print statement displays a rounded version.

## Scene 3 — Complete hours and leftover minutes

**Visual:** Show the complete-hours and remainder calculations separately. Use a simple timeline that groups 245 minutes into full hours and leftover minutes.

**Code**
```python
study_minutes = 245
full_hours = study_minutes // 60
leftover_minutes = study_minutes % 60
print(full_hours)
print(leftover_minutes)
```

**Expected output**
```text
4
5
```

**Narration:**

Normal division answers how many hours as a decimal. Floor division answers how many complete hours fit into the total. The percent operator gives the remainder after those full hours.

For two hundred and forty-five minutes, there are four complete hours and five minutes left over.

This is why floor division and modulo are useful together. They split a total into full units and a remainder.

## Scene 4 — Average session length

**Visual:** Use a separate fictional example. Show total minutes and session count, then the formula. Avoid the project's exact required test inputs.

**Code**
```python
total_minutes = 150
sessions = 5
average_session = total_minutes / sessions
print(round(average_session, 1))
```

**Expected output**
```text
30.0
```

**Narration:**

To calculate average session length, divide the total minutes by the number of sessions. In this example, one hundred and fifty minutes across five sessions gives an average of thirty minutes per session.

But there is an important edge case. What happens if the session count is zero? We cannot divide by zero.

A good function should check that case deliberately and return the required message, rather than letting the program crash or pretending the average is zero.

## Scene 5 — Design the report before implementing it

**Visual:** Show a field checklist only: total minutes, complete hours, leftover minutes, average session length. Show no completed report output.

**Narration:**

The project asks for a function named study_time_report. It receives total minutes and the number of sessions, and it should return a report containing the requested values.

Plan the report first. Decide what each field should mean, which operator produces it, and how the output should be formatted.

Remember that the function should return the report, not just print it. A returned value can be tested by the app and reused by other code.

I'm not going to show the complete function here. The important part is that you can explain each calculation and choose the correct operator for it.

## Scene 6 — Test normal and edge cases

**Visual:** Show test-case labels without completed outputs: a typical total, a small total, and zero sessions.

**Narration:**

Test more than one case.

A typical total checks the ordinary calculation. A small total helps you check that complete hours can be zero while leftover minutes still have a value. And zero sessions checks the special rule required by this project.

For each case, predict the output before running your function. If the result is wrong, inspect one calculation at a time: normal division, floor division, remainder, or rounding.

## Scene 7 — Reflection

**Visual:** Display “What question does each operator answer?” with slash, double slash, percent, and round.

**Narration:**

Before you finish, answer this question: why use floor division when normal division is available?

Normal division gives a decimal result. Floor division tells us how many complete units fit. Modulo tells us what remains. These operations are related, but they answer different questions.

## Final call to action — watch the practice video

**Visual:** Use a neutral end card reading “Next: Practice Video”. Do not show or describe unfinished PyLearn app screens or reveal a completed project solution.

**Narration:**

Great work! You've finished this lesson. The next step is to watch the practice video. I recommend watching it because it will help you apply what you've learned with a fresh example.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

**Visual:** Hold the “Next: Practice Video” end card long enough to read.

## Production and QA checklist

- [ ] Verify the exact approved Kendrick voice ID before generating audio.
- [ ] Use ElevenLabs v3 and the same approved voice throughout.
- [ ] Keep production notes out of spoken narration.
- [ ] Verify all demonstration code and output in Python.
- [ ] Do not show the full `study_time_report` implementation or the project's required test solutions.
- [ ] Preserve the project navigation ending and progression rule.
