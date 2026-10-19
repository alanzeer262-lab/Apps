# PyLearn Video 01 — Your First Python Program

**Voice lock — mandatory:** Kendrick voice; ElevenLabs v3; exact approved Kendrick voice ID must be inserted before narration generation; no substitution or preset; same voice throughout. **Voice ID status:** not present in the current repository files or voice-lock record reviewed; do not guess, select a similar voice, or generate narration until the approved ID is recovered from the original Runway setup.
**Canonical source:** `Pylearn-build260/content/python-basics/modules/01-first-program.md`
**Use:** Runway narration preparation. Do not send scene headings or stage directions to text-to-speech; send only the spoken narration. Review code/output against the source before generating audio.

## Lesson video standard

This is the full teaching video, not the practice video. Keep the lesson rich: explain the ideas, show code gradually, pause for predictions, demonstrate outputs and common mistakes, and recap. Do not shorten or remove teaching content to make room for practice. The ending must clearly direct learners to the Practice section in the PyLearn app, including people watching on YouTube.

## Scene 1 — First program

Welcome to PyLearn. I'm glad you're here.

In this lesson, we're going to write a tiny Python program together. You don't need to know anything about programming yet. We'll take it one step at a time.

Imagine you want the computer to show you a message. In Python, we can use a command called print.

Let's build the line slowly.

Inside the parentheses, we put the message we want Python to display. The quotation marks tell Python that this message is text.

Now let's run it.

Here it is: Hello, I'm Python.

You wrote a line of code, ran it, and saw the result. That's your first program.

We'll use this same habit again and again: write a little code, run it, and look carefully at what happened.

## Scene 2 — Python can calculate

Our first program displayed a message. Let's ask Python to do something a little different.

This time, we're giving it a small calculation: two plus three.

Before I run it, what number do you think Python will display? Take a moment to work it out.

Let's check.

First, we see the greeting. On the next line, we see five.

Python did the calculation for us, and print displayed the answer.

That's all we need to learn from this example: print can display a message, or it can display the result of a calculation.

## Scene 3 — Numbers and text

Look at these two lines. The first has the number ten. The second has the characters one and zero inside quotation marks.

They look almost the same, don't they?

Before we run them, make a prediction: will the output look different?

On the screen, both lines show ten. So the visible result looks the same.

But the quotation marks matter. They tell Python that the second value is text, not a number.

Text in Python is called a string. You don't need to memorize every detail right now. Just notice the difference: quotation marks tell us that we're working with text.

## Scene 4 — Matching quotation marks

Let's look at quotation marks a little more closely.

Python lets us use single quotes or double quotes around text. Both of these examples are valid.

Here's the rule to remember: the opening quote and the closing quote must match.

Now I'll make one small mistake in a separate example. Notice that I haven't closed the quotation marks.

Python reports an error because it can't understand where the text ends.

This is normal. Mistakes are part of programming. When you see an error, slow down and look at the line. Sometimes one small character is all that needs fixing.

## Scene 5 — Comments

Sometimes we want to leave a note for ourselves, or for the next person who reads our code.

In Python, a comment starts with the hash symbol. Here, the first line is a comment.

Python ignores that line when it runs the program. The next line is a command, so Python displays the message.

Notice the output: the message appears, but the comment does not.

That's the whole idea. A comment is a note for people reading the code.

## Scene 6 — Make the message personal

Let's make the message personal.

First, we store a name in a variable called name. For now, think of a variable as a named place where a value is kept.

Here, the value is Ada. On the next line, we use that value in a greeting.

The letter f tells Python that we want to place a value inside this message. The curly braces show where the value should go.

Let's run it.

Python puts Ada into the greeting.

Now let's change just one thing: the name.

Now the greeting says Sam. We didn't rewrite the whole message. We changed the value, and the result changed with it.

That's a useful idea. A program can use a value in a message, and when the value changes, the message can change too.

## Scene 7 — Showing a value versus returning it

**Visual:** Keep the same editor. Show both function definitions, then call them separately. Never show the output before the matching call is narrated.

**Narration:**

There's one important distinction in Python: showing a value is not the same as returning a value.

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

## Scene 8 — A placeholder in a function

**Visual:** Show an unfinished function with `pass`, then replace only that line with a real return statement.

**Code**
```python
def double(number):
    pass
```

**Narration:**

You may also see the word pass in starter code. Python needs a valid body inside a function. Pass is a placeholder that does nothing, allowing an unfinished function to run without a syntax error. When you complete the exercise, replace pass with your solution.

**Visual:** Replace `pass` with `return number * 2`; call `double(7)` and display the result.

**Code**
```python
def double(number):
    return number * 2

print(double(7))
```

**Expected output**
```text
14
```

**Narration:**

Now the function returns fourteen, and print displays it. You'll learn to write functions more fully later. For now, recognize pass as a placeholder, not the finished answer.

## Scene 9 — Your turn

Now it's your turn.

Change the name to your own name. Before you run the program, predict what the message will say.

Take your time.

Now run it and check your prediction.

If the message doesn't look right, check the quotation marks first. Then check the braces around the variable name.

You've just practiced changing a value and using it in a message.

## Scene 10 — Debugging calmly

Let's practice fixing the small mistake we saw earlier.

This line is missing its closing quotation mark.

When an error appears, don't change lots of things at once. Look at the line, find the likely problem, and change just one thing.

Now it works.

Remember this simple routine: read the error, check the line, change one thing, and run again. You don't have to panic when code doesn't work. You can investigate it step by step.

## Scene 11 — Recap

Let's take a breath and review what you've done.

You used print to display a message and a calculation. You saw that quotation marks tell Python when a value is text. You learned that comments are notes for people reading the code.

Then you used a variable to store a name, and an f-string to place that name inside a message. You learned the difference between print and return, saw why a print-only function gives back None, and recognized pass as a placeholder. Finally, you practiced fixing a small error by changing one thing at a time.

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

- [ ] Lesson remains a full teaching video; do not trim concepts to make room for practice.
- [ ] Code and output match exactly, and output is revealed only after the matching narration.
- [ ] The final card explicitly names the PyLearn app's Practice section.
- [ ] YouTube viewers are explicitly told to open PyLearn and find the matching lesson practice.
- [ ] The ending does not reveal exercise solutions.
- [ ] Full video is reviewed at normal speed before it is marked complete.
