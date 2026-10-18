# PyLearn Video 02 — Variables and Data Types

**Course:** Python Basics  
**Lesson:** 02 — Variables and Data Types  
**Purpose:** Complement the existing reading lesson; do not replace or edit it.  
**Audience:** Beginners  
**Target runtime:** 5–6 minutes, depending on the teacher's pace and learner pauses.  
**Format:** Patient teacher-led narration, one continuous code editor, one output panel.  
**Continuity:** Reuse Lesson 1's established dark editor/terminal visual language, typography, layout, and teacher delivery. Keep examples connected in the same file.

## Teaching goal

By the end, the learner should be able to:
1. Explain a variable as a name that refers to a value.
2. Assign a value and use the variable in an expression.
3. Recognize the beginner-level types `str`, `int`, `float`, and `bool`.
4. inspect a value's type with `type()`.
5. Predict what changes when a variable's value changes.

Keep this lesson focused. Do not introduce lists, dictionaries, loops, functions, input(), or detailed type conversion.

## Production rules

- Speak naturally and patiently; do not read headings or stage directions aloud.
- Introduce one idea at a time. Pause before running code when asking for a prediction.
- Reveal code in small meaningful chunks, then run it. Keep code and its matching output visible together.
- Use the actual outputs below; do not invent terminal results.
- Keep the same editor and terminal throughout. Extend or edit the current example rather than cutting to unrelated slides.
- Use spoken phrases as synchronization anchors. Final timings must be generated from the approved recorded narration by the existing GitHub transcript-alignment workflow. Never guess timestamps or stretch audio.
- The script/storyboard is a production draft until checked against the source reading lesson and approved narration.

## Scene overview

| Scene | Teaching focus | Main visual beat |
|---|---|---|
| 1. Give a value a name | Variable assignment | Introduce `name = "Sam"` |
| 2. Use the variable | Reuse and update a value | Print a greeting, change Sam to Ada, run again |
| 3. Numbers are values too | Integer and float | Show `age = 12` and `height = 1.5` |
| 4. Different kinds of values | String, integer, float, boolean | Label values without overloading the learner |
| 5. Ask Python about a type | `type()` | Run a small type-check example |
| 6. Learner prediction and recap | Apply the idea | Ask what changes when one assignment changes |

---

## Scene 1 — Give a value a name

**Code to reveal**
```python
name = "Sam"
print(name)
```

**Expected output**
```text
Sam
```

**Teacher narration**

“In the last lesson, we asked Python to display messages and calculate numbers.

Now let's make our programs easier to change.

Imagine we want to use someone's name more than once. Instead of typing the name into every line, we can give that value a name of its own.

Watch this line: `name = "Sam"`.

The word on the left is the variable name. The value on the right is what we assign to it. The equals sign means assignment here: it tells Python to associate the name with that value.

Now let's print the variable.”

[Reveal `print(name)`, pause briefly, then run.]

“The output is Sam. Notice that we wrote `name` without quotation marks in the print statement. We're asking Python to look up the value stored under that variable name.”

**Visual notes:** Highlight `name`, then `"Sam"`, then the output. Distinguish quoted text from the unquoted variable name.

**Spoken anchor:** “The output is Sam.”

---

## Scene 2 — Use the variable again

**Code to extend**
```python
name = "Sam"
print(f"Hello, {name}!")
```

**Expected output**
```text
Hello, Sam!
```

**Teacher narration**

“We can use that same variable inside a message.

This is an f-string. The letter f before the quote tells Python to fill in values inside the curly braces. Here, the braces contain our variable name.

Before we run it, what do you think the message will say?”

[Pause for two seconds, then run.]

“It says, ‘Hello, Sam!’ Now let's change just one thing.”

[Change `"Sam"` to `"Ada"`; leave the print line unchanged; run again.]

“The message now says, ‘Hello, Ada!’ We didn't have to rewrite the greeting. We changed the value in one place, and the program used the new value.”

**Visual notes:** Keep the print line unchanged while editing the assignment. Briefly compare both outputs, then leave the new output visible.

**Spoken anchor:** “We changed the value in one place.”

---

## Scene 3 — Numbers are values too

**Code to extend**
```python
name = "Ada"
age = 12
height = 1.5

print(name)
print(age)
print(height)
```

**Expected output**
```text
Ada
12
1.5
```

**Teacher narration**

“Variables can hold more than text.

Here, `age` is assigned the whole number twelve. And `height` is assigned the decimal number one point five.

When Python sees the number twelve without quotation marks, it treats it as a number, not as text. The decimal value is also numeric.

Let's run these lines and see the values.”

[Reveal the print lines, then run.]

“We see Ada, twelve, and one point five. The print statements display each value. The values themselves have different kinds, and Python can work with those kinds in different ways.”

**Visual notes:** Reveal assignments one at a time. Keep quoted text, whole number, and decimal number visually distinguishable. Avoid decorative numeric animations that imply a different result.

**Spoken anchor:** “The values themselves have different kinds.”

---

## Scene 4 — Four common kinds of values

**Code to reveal**
```python
name = "Ada"
age = 12
height = 1.5
is_learning = True
```

**Teacher narration**

“Let's name four common kinds of values.

Text inside quotes is a string, written as `str`.

A whole number, like twelve, is an integer, written as `int`.

A number with a decimal point, like one point five, is a float, written as `float`.

And a value that represents true or false is a Boolean, written as `bool`. In Python, the Boolean values are spelled `True` and `False`, with capital letters.

You don't need to memorize everything at once. For now, notice the clues: quotes for text, a whole number, a decimal number, and a true-or-false value.”

**Visual notes:** Highlight one assignment at a time and show a small matching label beside it: string, integer, float, Boolean. Keep all four lines readable.

**Spoken anchor:** “For now, notice the clues.”

---

## Scene 5 — Ask Python about a type

**Code to extend**
```python
print(type(name))
print(type(age))
print(type(height))
print(type(is_learning))
```

**Expected output**
```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

**Teacher narration**

“Python can tell us the type of a value.

The `type()` function asks Python what kind of value it is looking at. Let's check each variable.”

[Run and reveal the four output lines.]

“The results match what we just learned: string, integer, float, and Boolean.

You won't need to call `type()` every time you write a program, but it's a useful tool when you're learning or checking an unexpected result.”

**Visual notes:** Reveal outputs line by line. Make the type names readable; don't claim the angle-bracket output is a value the learner should type.

**Spoken anchor:** “The results match what we just learned.”

---

## Scene 6 — Your turn

**On-screen challenge — do not show an answer**

“Pause and predict: if we change `age = 12` to `age = 13`, which output will change? What will the new output be?”

[Leave the code and question on screen for 4 seconds. Do not reveal the answer in this scene.]

**Teacher narration**

“Think about the lines that use `age`. The value is assigned once, and the program reads that value when it runs. Try changing the age yourself, then run the program and compare the result with your prediction.”

## Recap and close

**Teacher narration**

“Let's recap.

A variable gives a value a name. You can use that name again, and when you assign a different value, the program can use the updated value.

Python has different types of values. Strings are text, integers are whole numbers, floats are numbers with decimal points, and Booleans are true-or-false values. The `type()` function can help you inspect them.

You don't need to master every detail in one sitting. Practice changing one value, running the code, and observing what happens.

In the next lesson, we'll build on these ideas with more practice using values in Python. Nice work!”

**End screen:** “Variables and Data Types — Complete” and “Keep Practicing”.

Hold for approximately 3 seconds after the final spoken word.

---

## Quality checklist

- [ ] Narration has a calm pace and genuine pauses.
- [ ] Variable assignment is explained without saying that `=` means mathematical equality.
- [ ] The variable name `name` is shown without quotes in `print(name)`.
- [ ] The f-string output changes from Sam to Ada by editing only the assignment.
- [ ] The code and outputs match exactly.
- [ ] `True` is capitalized and `type()` output uses Python's real type names.
- [ ] The prediction question appears before any answer.
- [ ] Visuals keep the Lesson 1 editor, terminal, typography, and palette.
- [ ] Transcript-derived anchors are validated against the actual approved audio.
- [ ] Full video is reviewed at normal speed before it is marked complete.
