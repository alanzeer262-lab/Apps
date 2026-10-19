# PyLearn Video 12 — Project 1: My Learning Report

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generating audio.
> - No guessed ID, substitution, or preset. Keep the same approved voice across all parts.
> - Speak narration only. Do not read headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/12-build-personal-report.md`, branch `ccr-c7f6fdd7-xpzi3g`.  
**Target runtime:** Approximately 5–7 minutes.  
**Project-video rule:** Teach the approach without showing the complete required function or its finished solution.

## Scene 1 — From small lessons to a useful program

**Visual:** Show a clean editor and the title “Project 1: My Learning Report.” Briefly display the kinds of information a learner report needs: name, goal, weekly study hours, and active status. Do not show a completed required function.

**Narration:**

Welcome to your first Python Basics project.

So far, you've learned how to store values, choose clear variable names, and display readable messages. Now we're going to use those skills to think about a small, useful program: a learning report.

Imagine a report that tells us a learner's name, their goal, how many hours they study each week, and whether they're currently active.

The goal of this project is not to memorize a finished block of code. It's to take a clear requirement, break it into pieces, and build the solution yourself.

## Scene 2 — Identify the inputs

**Visual:** Reveal four variables using a fictional example. Do not combine them into the completed project function.

**Code**
```python
name = "Ada"
goal = "Data Analyst"
weekly_hours = 6
active = True
```

**Narration:**

Let's identify the information before thinking about the report itself.

Name and goal are text. Weekly hours is a number. Active is a Boolean, which means it represents true or false.

Notice that these values have different types because they represent different kinds of information. Clear names help us understand what each value means.

Before building a function, make sure you know what information it needs. In this project, those four values are the inputs.

## Scene 3 — Turn a Boolean into readable status text

**Visual:** Use an unrelated small example to demonstrate a decision without completing the project function.

**Code**
```python
is_open = True

if is_open:
    status = "Open"
else:
    status = "Closed"

print(status)
```

**Expected output**
```text
Open
```

**Narration:**

One of the report's fields is an active or inactive status. A Boolean is useful inside the program, but the final report should use words a person can understand.

Here's a separate example. If is_open is true, the program chooses Open. Otherwise, it chooses Closed.

The same general idea can help us turn a true-or-false value into readable text. I'm using an unrelated example here so you can practice the technique without seeing the finished project solution.

## Scene 4 — Return text rather than only printing it

**Visual:** Contrast a print statement with a returned string. Use a small greeting example rather than the required report function.

**Code**
```python
def make_greeting(name):
    return f"Welcome, {name}!"

message = make_greeting("Lin")
print(message)
```

**Expected output**
```text
Welcome, Lin!
```

**Narration:**

This project asks you to build a function that returns a report. Remember the difference between print and return.

Print displays text on the screen. Return hands a value back to the code that called the function. Returning a string lets another part of the program decide when and where to display it.

In this example, the function returns a greeting. We store the returned string in message, and then print it. Your project will use the same general idea, but you'll build the report from the required inputs.

## Scene 5 — Design the output before coding

**Visual:** Show an empty four-line report template, with field labels only. Do not populate the complete report with the required example values.

**On-screen template**
```text
Learner: [name]
Goal: [goal]
Weekly study hours: [weekly hours]
Status: [status]
```

**Narration:**

Before you write the full function, look at the format the report should follow.

It has four lines. Each line has a label and a value. Planning the output first helps you check whether your function includes every required field and uses the exact format expected by the tests.

Think about how an f-string could place each value inside a readable line. Then think about how the four lines can be combined into one returned string.

Don't rush to write everything at once. Build one piece, check it, and then add the next.

## Scene 6 — Test meaningful cases

**Visual:** Show a test checklist, not the function solution: typical learner, zero weekly hours, inactive learner. Do not reveal complete expected output for all required tests.

**Narration:**

A good program should work for more than one convenient example.

The project asks you to test a normal learner, a learner with zero study hours, and an inactive learner.

Why are these cases useful? The normal case checks the basic format. Zero hours checks whether your program handles a valid boundary value. An inactive learner checks whether your status logic can represent the other Boolean value.

For each test, compare the returned report with the required format. If something is wrong, change one thing at a time and run the test again.

## Scene 7 — Reflection

**Visual:** Show two headings: “Measurements” and “Descriptions.” Ask the learner to classify name, goal, and weekly hours mentally.

**Narration:**

Before you finish, consider this question: which values are measurements, and which values are descriptions?

Weekly study hours is a measurement. A name and a goal describe the learner. Thinking about the meaning of each field helps you choose the right type and the right output format.

## Project closing — required for in-app and YouTube versions

**Visual:** Show the real PyLearn navigation path to the “My learning report” project task. Do not show the completed function, its full output, or unverified app screens. Hold the task name on screen long enough to read.

**Narration:**

Now open PyLearn and find the My Learning Report task.

Build it yourself and run the tests. This video has shown the ideas, not the finished solution. Practice Drills, if shown, are optional; complete and pass the required project exercise to unlock the next lesson.

Pause the video and start building.

## Production and QA checklist

- [ ] Verify the exact approved Kendrick voice ID before generating audio.
- [ ] Use ElevenLabs v3 and the same approved voice identity throughout.
- [ ] Keep production notes out of spoken narration.
- [ ] Verify every demonstration code sample and expected output in Python.
- [ ] Do not show the complete `build_learning_report` function or finished required output.
- [ ] Use only verified app navigation visuals.
- [ ] Preserve the project-specific navigation ending and progression rule.
