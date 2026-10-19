# PyLearn Video 01 — Your First Python Program

**Voice lock — mandatory:** Kendrick voice; ElevenLabs v3; exact approved Kendrick voice ID must be inserted before narration generation; no substitution or preset; same voice throughout. **Voice ID status:** not present in the current repository files or voice-lock record reviewed; do not guess, select a similar voice, or generate narration until the approved ID is recovered from the original Runway setup.
**Canonical source:** `Pylearn-build260/content/python-basics/modules/01-first-program.md`
**Use:** Runway narration preparation. Do not send scene headings or stage directions to text-to-speech; send only the spoken narration. Review code/output against the source before generating audio.

## Lesson video standard

This is the full teaching video, not the practice video. Keep the lesson rich: explain the ideas, show code gradually, pause for predictions, demonstrate outputs and common mistakes, and recap. Do not shorten or remove teaching content to make room for practice. The ending must clearly direct learners to the Practice section in the PyLearn app, including people watching on YouTube.

## Scene 1 — First program

**Visual:** Start with an empty editor. Reveal the code one line at a time. Highlight `print`, then the parentheses, then the quoted message. Run only after the full line is visible.

Welcome to PyLearn. I'm glad you're here.

In this lesson, we'll write a small Python program together. You can start without knowing programming. We'll take it one step at a time.

Imagine you want the computer to introduce itself. What is the smallest program that can do that?

**Code**
```python
print("Hello, I'm Python.")
```

In this line, `print` asks Python to display something. The parentheses contain what we want to display, and the quotation marks tell Python that the message is text.

**Visual:** Run the line. Reveal the output only after the run.

**Output**
```text
Hello, I'm Python.
```

You wrote a line of code, ran it, and saw the result. That's your first program.

We'll use the same habit throughout the course: write a little code, run it, and observe what happened.

## Scene 2 — Python can calculate

**Visual:** Keep the first example visible, then add a second line beneath it. Ask for a prediction before running the two lines.

Our first program displayed a message. Let's ask Python to do something a little different. This time, we're giving it a small calculation: two plus three.

**Code**
```python
print("Hello, I'm Python.")
print(2 + 3)
```

Before I run it, what number do you think Python will display? Take a moment to work it out.

**Visual:** Run both lines. Reveal the output line by line.

**Output**
```text
Hello, I'm Python.
5
```

Python did the calculation for us, and `print` displayed the answer. That's all we need to learn from this example: `print` can display a message, or it can display the result of a calculation.

## Scene 3 — Numbers and text

**Visual:** Show the two lines together, with no output yet.

Look at these two lines. The first contains the number ten. The second contains the characters one and zero inside quotation marks.

They look almost the same, don't they? Before we run them, predict: will the output look different?

**Code**
```python
print(10)
print("10")
```

**Visual:** Run both lines and reveal the two output lines.

**Output**
```text
10
10
```

The visible output looks the same, but Python treats the values differently. Quotation marks tell Python that the second value is text. Text in Python is called a string.

You don't need to master data types yet. For now, remember that quotation marks matter; in the next lesson, you'll look more closely at how Python distinguishes different kinds of values.

## Scene 4 — Matching quotation marks

**Visual:** Show valid examples first, then the broken example in a separate run so the error does not interrupt the valid code.

Python lets us use single quotes or double quotes around text. Both are valid.

**Code**
```python
print("Hello")
print('Hello')
```

**Output**
```text
Hello
Hello
```

Here's the rule to remember: the opening quote and the closing quote must match.

Now let's make one small mistake in a separate example.

**Broken code — run separately**
```python
print("Hello)
```

Python reports a syntax error because it can't tell where the text ends. This is normal. When you see an error, slow down and inspect the line. Sometimes one small character is all that needs fixing.

## Scene 5 — Comments

Sometimes we want to leave a note for ourselves, or for the next person who reads our code.

**Code**
```python
# This line explains the program
print("The code still runs.")
```

In Python, a comment starts with the hash symbol. Python ignores that line when it runs the program. The next line is a command, so Python displays the message.

**Output**
```text
The code still runs.
```

Notice that the message appears, but the comment does not. A comment is a note for people reading the code.

## Scene 6 — Make the message personal

**Visual:** Reveal the variables first; then reveal the print statements. Do not show the output until the code is run.

Let's make the message personal. A variable is a name we use to refer to a value. Here, we'll store three pieces of information: a name, a learning goal, and the number of hours we plan to study each week.

**Code**
```python
name = "Ada"
goal = "data analysis"
hours = 6

print(f"My name is {name}.")
print(f"My goal is to learn {goal}.")
print(f"I plan to study {hours} hours each week.")
```

The letter `f` before a string tells Python to place the values inside the curly braces into the message. Notice that each line is still a message, but the values come from our variables.

**Visual:** Run the code. Reveal each output line as it appears.

**Output**
```text
My name is Ada.
My goal is to learn data analysis.
I plan to study 6 hours each week.
```

Now change only the name from Ada to Sam and run it again. The name in the first sentence changes, while the goal and hours stay the same.

The same idea works for the other values. Change the goal or the number of hours and predict which sentence will change before you run the program.

This is the point of variables and f-strings: store values once, then use them to make clear, readable messages.

## Scene 7 — Showing a value versus returning it

**Visual:** Put a small on-screen label beside the code: “You don't need to design functions from scratch yet.” Keep the editor simple. Show both function definitions, then run each example separately. Never show output before its matching call.

**Narration:**

The app will sometimes give you a function starter to complete. You do not need to learn how to design whole functions from scratch in this lesson. But you do need to recognize one important distinction: showing a value is not the same as returning a value.

The print command displays something on the screen. A return statement hands a value back to the part of the program that called the function, so the program can use it again.

Let's compare two small functions.

**Code to reveal**
```python
def show_total(bill):
    print(bill + 10)

def add_tip(bill):
    return bill + 10
```

**Narration:**

These are function definitions, so nothing is displayed just by defining them. The first function prints the total. The second returns the total.

**Visual:** Run `total = add_tip(40)`, then reveal the print calls in order.

**Code**
```python
total = add_tip(40)
print(f"You pay: {total}")
print(f"For a table of two: {total * 2}")
```

**Expected output**
```text
You pay: 50
For a table of two: 100
```

**Narration:**

The function returns fifty. We store that answer, print it, and then use it again to calculate one hundred. Returning a value lets the rest of the program keep working with the answer.

**Visual:** Now run the print-only version.

**Code**
```python
saved = show_total(40)
print(saved)
```

**Expected output**
```text
50
None
```

**Narration:**

The first line displays fifty. But because show_total doesn't return a value, the variable saved receives None. That is why the next line displays None. Remember: print talks to the person looking at the screen; return gives a value back to the code.

## Scene 8 — Recognize a placeholder in starter code

**Visual:** Show a provided unfinished function starter. Do not reveal or complete the app exercise's actual code.

**Code**
```python
def double(number):
    pass
```

You may see the word `pass` in starter code. Python needs a valid body inside a function, and `pass` is a placeholder that does nothing. It lets an unfinished function remain syntactically valid. In an exercise, you replace `pass` with your own solution. For now, the goal is simply to recognize what the placeholder means. You do not need to design a function from scratch.

## Scene 9 — Your turn

Now it's your turn. Using the example from the previous scene as a guide, make a small introduction program of your own.

Store your name, a learning goal, and the number of hours you plan to study each week. Print each value in a readable sentence using an f-string.

Before you run the program, predict what each sentence will say. Then run it and check your prediction. Change one value and predict which sentence will change.

If a message doesn't look right, check the quotation marks first, then check the braces around each variable name. Keep this example separate from the required in-app exercise: it is practice to help you prepare, not its answer.

## Scene 10 — Use a calm debugging routine

**Visual:** Return briefly to the earlier line with the missing closing quote. Highlight the missing character, add it, and run again.

Let's apply the routine to the quotation-mark mistake we saw earlier. The error tells us Python could not understand the line. We inspect the punctuation, add the missing closing quote, and run it again.

When code doesn't work, change one thing at a time. That makes it easier to see which change fixed the problem. An error is information that helps you investigate.

## Scene 11 — Recap

Let's take a breath and review what you've done.

You used print to display a message and a calculation. You saw that quotation marks tell Python when a value is text. You learned that comments are notes for people reading the code.

Then you used variables to store a name, a learning goal, and weekly study hours, and used f-strings to place those values inside readable messages. You learned the basic difference between `print` and `return`, saw why a print-only function gives back `None`, and recognized `pass` as a placeholder in starter code. Finally, you practiced fixing a small error by changing one thing at a time.

You don't need to remember every detail perfectly today. The important thing is that you've written code, run it, observed the result, and made a change yourself.

That's a real first step into programming.

In the next lesson, we'll explore variables and data types more carefully. For now, take a moment to be proud of what you've built.

Your first Python program is complete.

## Final call to action — required for YouTube and in-app versions

**Visual:** Show the PyLearn app and clearly highlight the Practice section for Lesson 1. Do not show completed exercise answers. Leave the call to action on screen long enough to read.

**Narration — preserve this navigation instruction in both the in-app and YouTube versions:**

Now it's your turn to write code yourself.

Open PyLearn and go to Lesson 1. Complete its required coding exercise. If you're watching this on YouTube, open PyLearn and find this same lesson there.

Write your code, run it, read the feedback, and fix mistakes as needed. Practice Drills are optional. Passing the required exercise is what unlocks the next lesson.

Pause this video and start coding.

**Visual:** Show the real PyLearn navigation path to Lesson 1 and highlight the required coding exercise. Do not show a completed answer or unverified UI. Hold the final screen long enough to read.

## Production checklist

- [ ] The example includes name, learning goal, and weekly study hours, matching the canonical Lesson 1 source.
- [ ] Function examples are explicitly framed as recognizing provided starter code, not learning to design functions from scratch.
- [ ] Repeated debugging explanation is reduced; the second occurrence applies the earlier idea.
- [ ] Lesson remains a full teaching video; do not trim concepts to make room for practice.
- [ ] Code and output match exactly, and output is revealed only after the matching narration.
- [ ] The final card explicitly names the PyLearn app's Practice section.
- [ ] YouTube viewers are explicitly told to open PyLearn and find the matching lesson practice.
- [ ] The ending does not reveal exercise solutions.
- [ ] Full video is reviewed at normal speed before it is marked complete.
