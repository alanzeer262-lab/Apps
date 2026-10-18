# PyLearn Video 01 — Your First Python Program
## Revised patient-tutor script (pilot version 2)

**Audience:** Complete beginner  
**Purpose:** Help the learner write, run, and understand a tiny first program.  
**Target:** About 6–8 minutes, including purposeful pauses and code demonstrations.  
**Teacher style:** Warm, calm, clear, conversational. Never rush to fill silence.

## Scope change
This version intentionally removes the deep dive into functions, `return`, and `None`. Those are important ideas, but they belong in a dedicated lesson. The first video should give the learner a successful first experience, not a tour of too many concepts.

## Production rules
- Keep one editor and one output panel throughout.
- Reveal code in small chunks; never show a completed example before the teacher has introduced it.
- Speak the exact words in the narration. Bracketed stage directions are not spoken.
- Use pauses for prediction or practice, not to disguise rushed narration.
- Keep code and real output visible together. Do not fabricate output or error text.
- Preserve the synchronization workflow, but regenerate narration and update cue phrases to match this script before rendering.

---

## Scene 1 — We can ask Python to speak

**Goal:** Run one line and understand what `print()` does.

**Visual:** Start with an empty editor. Reveal `print`, then the opening parenthesis, quoted message, and closing characters in short chunks.

**Code**
```python
print("Hello, I'm Python.")
```

**Output**
```text
Hello, I'm Python.
```

**Narration**

“Welcome to PyLearn. I'm glad you're here.

In this lesson, we're going to write a tiny Python program together. You don't need to know anything about programming yet. We'll take it one step at a time.

Imagine you want the computer to show you a message. In Python, we can use a command called `print()`.

Let's build the line slowly.”

[Reveal the code in short chunks. Hold until the full line is easy to read.]

“Inside the parentheses, we put the message we want Python to display. The quotation marks tell Python that this message is text.

Now let's run it.”

[Run the code. Keep the line and output visible.]

“Here it is: ‘Hello, I'm Python.’

You wrote a line of code, ran it, and saw the result. That's your first program.

We'll use this same habit again and again: write a little code, run it, and look carefully at what happened.”

[Pause briefly before moving on.]

---

## Scene 2 — Python can calculate

**Goal:** See that `print()` can display a calculation, not just a message.

**Visual:** Keep the first example in editor history. Add a second line and highlight only `2 + 3`.

**Code**
```python
print("Hello!")
print(2 + 3)
```

**Output**
```text
Hello!
5
```

**Narration**

“Our first program displayed a message. Let's ask Python to do something a little different.

This time, we're giving it a small calculation: two plus three.”

[Show the line but do not run it yet.]

“Before I run it, what number do you think Python will display? Take a moment to work it out.”

[Pause for 4 seconds.]

“Let's check.”

[Run both lines.]

“First, we see the greeting. On the next line, we see five.

Python did the calculation for us, and `print()` displayed the answer.

That's all we need to learn from this example: `print()` can display a message, or it can display the result of a calculation.”

[Leave both output lines visible long enough to read.]

---

## Scene 3 — Numbers and text can look alike

**Goal:** Introduce the difference between a number and text without overloading the learner.

**Visual:** Show the two lines. Highlight the quotation marks around the second value.

**Code**
```python
print(10)
print("10")
```

**Output**
```text
10
10
```

**Narration**

“Look at these two lines. The first has the number ten. The second has the characters one and zero inside quotation marks.

They look almost the same, don't they?

Before we run them, make a prediction: will the output look different?”

[Pause for 4 seconds, then run.]

“On the screen, both lines show ten. So the visible result looks the same.

But the quotation marks matter. They tell Python that the second value is text, not a number.

Text in Python is called a string. You don't need to memorize every detail right now. Just notice the difference: quotation marks tell us that we're working with text.”

[Hold on the code and output together.]

---

## Scene 4 — Matching quotation marks

**Goal:** Learn one simple rule for writing text safely.

**Visual:** Show a valid example, then a separate intentional mistake. Clearly label the mistake as a demonstration.

**Valid code**
```python
print("Hello")
print('Hello')
```

**Output**
```text
Hello
Hello
```

**Intentional error example**
```python
print("Hello)
```

**Narration**

“Let's look at quotation marks a little more closely.

Python lets us use single quotes or double quotes around text. Both of these examples are valid.”

[Run the valid example and show the two lines of output.]

“Here's the rule to remember: the opening quote and the closing quote must match.

Now I'll make one small mistake in a separate example. Notice that I haven't closed the quotation marks.”

[Run the intentionally broken example and show the real interpreter error.]

“Python reports an error because it can't understand where the text ends.

This is normal. Mistakes are part of programming. When you see an error, slow down and look at the line. Sometimes one small character is all that needs fixing.”

[Restore valid code.]

---

## Scene 5 — Leave a note for people

**Goal:** Understand that a comment is for readers and does not run as code.

**Code**
```python
# This is a note for a person
print("The program still works.")
```

**Output**
```text
The program still works.
```

**Narration**

“Sometimes we want to leave a note for ourselves, or for the next person who reads our code.

In Python, a comment starts with the hash symbol. Here, the first line is a comment.”

[Highlight the hash symbol and comment.]

“Python ignores that line when it runs the program. The next line is a command, so Python displays the message.”

[Run the example.]

“Notice the output: the message appears, but the comment does not.

That's the whole idea. A comment is a note for people reading the code.”

[Give the learner a moment to compare the editor and output.]

---

## Scene 6 — Make the message your own

**Goal:** Personalize one message using a variable and an f-string. Keep the explanation concrete.

**Code — first run**
```python
name = "Ada"
print(f"Hello, {name}!")
```

**Output**
```text
Hello, Ada!
```

**Code — change one value**
```python
name = "Sam"
print(f"Hello, {name}!")
```

**Output**
```text
Hello, Sam!
```

**Narration**

“Let's make the message personal.

First, we store a name in a variable called `name`. For now, think of a variable as a named place where a value is kept.”

[Reveal the first line and hold.]

“Here, the value is Ada. On the next line, we use that value in a greeting.”

[Reveal the print line. Highlight the letter f and the braces around name.]

“The letter `f` tells Python that we want to place a value inside this message. The curly braces show where the value should go.

Let's run it.”

[Run and show the output.]

“Python puts Ada into the greeting.

Now let's change just one thing: the name.”

[Change Ada to Sam. Run again.]

“Now the greeting says Sam. We didn't rewrite the whole message. We changed the value, and the result changed with it.

That's a useful idea. A program can use a value in a message, and when the value changes, the message can change too.”

[Keep the code and both results visible briefly, or show the old and new result side by side.]

---

## Scene 7 — Your turn

**Goal:** Give the learner one manageable task without showing a finished answer.

**Starter code**
```python
name = "Your name"
print(f"Hello, {name}!")
```

**Narration**

“Now it's your turn.

Change the name to your own name. Before you run the program, predict what the message will say.

Take your time.”

[Leave the code visible for 5 seconds. Do not reveal another answer.]

“Now run it and check your prediction.

If the message doesn't look right, check the quotation marks first. Then check the braces around the variable name.

You've just practiced changing a value and using it in a message.”

---

## Scene 8 — A simple debugging habit

**Goal:** Give the learner one calm, repeatable way to respond to a mistake.

**Broken code**
```python
print("Welcome to Python)
```

**Corrected code**
```python
print("Welcome to Python")
```

**Output after correction**
```text
Welcome to Python
```

**Narration**

“Let's practice fixing the small mistake we saw earlier.

This line is missing its closing quotation mark.”

[Run it and show the actual error.]

“When an error appears, don't change lots of things at once. Look at the line, find the likely problem, and change just one thing.”

[Add only the closing quote. Run again.]

“Now it works.

Remember this simple routine: read the error, check the line, change one thing, and run again. You don't have to panic when code doesn't work. You can investigate it step by step.”

---

## Scene 9 — Recap and next step

**Visual:** Show a few small examples from the lesson, one at a time. Do not crowd the screen.

**Narration**

“Let's take a breath and review what you've done.

You used `print()` to display a message and a calculation. You saw that quotation marks tell Python when a value is text. You learned that comments are notes for people reading the code.

Then you used a variable to store a name, and an f-string to place that name inside a message. Finally, you practiced fixing a small error by changing one thing at a time.

You don't need to remember every detail perfectly today. The important thing is that you've written code, run it, observed the result, and made a change yourself.

That's a real first step into programming.

In the next lesson, we'll explore variables and data types more carefully. For now, take a moment to be proud of what you've built.

Your first Python program is complete.”

**End card:**  
**Your First Python Program — Complete**  
**Next: Variables and Data Types**

[Hold the end card for 3 seconds without narration.]

---

## Review checklist
- [ ] Teacher sounds calm and conversational, not rushed.
- [ ] Each new idea is introduced before the code appears.
- [ ] The code is revealed in small readable chunks.
- [ ] Prediction pauses last about 3–5 seconds.
- [ ] Code and genuine output remain visible together.
- [ ] The learner gets a small task and time to attempt it.
- [ ] No function/return/None deep dive in this first video.
- [ ] The complete rendered video is reviewed before approval.
