# PyLearn Video 10 — Functions

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generating audio.
> - No guessed ID, substitution, or preset. Use the same approved voice identity throughout.
> - Speak narration only. Do not read headings or bracketed directions aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/10-functions.md`, branch `ccr-c7f6fdd7-xpzi3g`.  
**Target runtime:** Approximately 7–8 minutes. Do not reveal the required app exercise solution.

## Scene 1 — Give reusable logic a name

**Visual:** Start with a small repeated calculation, then introduce a function definition. Maintain the established editor and output panel.

**Narration:**

Welcome back to PyLearn.

Imagine you calculate an average in three different places in a program. If the calculation changes, you might need to update it in all three places.

A function lets us give a piece of logic a name and reuse it. Instead of copying the same steps, we define them once and call them when we need them.

Let's start with a small example.

**Code**
```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Ada")
print(message)
```

**Expected output**
```text
Hello, Ada!
```

**Narration:**

The first line defines a function named greet. The indented line is the function body. Later, we call greet with Ada, store the returned message in a variable, and print it.

Notice that defining a function and calling a function are two different actions. Python does not immediately run the body just because it has read the definition. The body runs when we call the function.

## Scene 2 — Parameters and arguments

**Visual:** Highlight `name` in the definition, then `"Ada"` in the call. Use two concise labels: parameter and argument.

**Narration:**

Let's look at the input to this function.

In the definition, name is a parameter. It is a variable that receives a value when the function is called.

In the call greet with Ada, the text Ada is the argument. It's the value we pass into the function.

Think of the process as input, function, result. The argument provides the input, the function uses that input, and the return statement provides the result.

Now change only the argument.

**Code**
```python
print(greet("Lin"))
```

**Expected output**
```text
Hello, Lin!
```

**Narration:**

The same function now greets Lin. We didn't rewrite the function. We supplied a different argument, and the function used that value.

This is one of the main benefits of functions: one clear piece of logic can work with many different inputs.

## Scene 3 — print and return are different

**Visual:** Show two small functions separately. Do not reveal output before the call is run.

**Code**
```python
def show_double(number):
    print(number * 2)

def double(number):
    return number * 2
```

**Narration:**

There is an important distinction between print and return.

Print displays something on the screen. Return hands a value back to the code that called the function, so the program can store that value or use it in another calculation.

These two functions may look similar, but they behave differently. The first displays the doubled number. The second returns the doubled number.

Let's call the returning version.

**Code**
```python
result = double(7)
print(result)
print(result + 3)
```

**Expected output**
```text
14
17
```

**Narration:**

The function returns fourteen. We store that value in result, print it, and then use it again by adding three.

A returned value can continue through the program. A printed message is only displayed; it is not automatically handed back as a reusable result.

For reusable logic, return is usually more useful than printing inside the function.

## Scene 4 — Give a function one clear job

**Visual:** Show the function name, input, and returned calculation. Reveal the call afterward.

**Code**
```python
def average_score(scores):
    return sum(scores) / len(scores)

result = average_score([10, 20, 30])
print(result)
```

**Expected output**
```text
20.0
```

**Narration:**

This function calculates an average. Its name tells us what job it performs, and its parameter scores tells us what input it needs.

Inside the function, sum adds the values and len counts them. The division produces the average, and return hands that answer back to the caller.

A function is easier to understand when it has one clear job. Avoid combining several unrelated tasks into one large function. Small functions are easier to read, test, and change.

## Scene 5 — Default parameters

**Visual:** Highlight the default value in the function definition, then show one call that uses it and another that overrides it.

**Code**
```python
def passed(score, cutoff=70):
    return score >= cutoff

print(passed(80))
print(passed(80, 90))
```

**Expected output**
```text
True
False
```

**Narration:**

A parameter can have a default value. Here, cutoff defaults to seventy.

When we call passed with only eighty, Python uses seventy as the cutoff, so the result is true.

When we provide a second argument, ninety, that value replaces the default for this call. Eighty is not at least ninety, so the result is false.

Defaults are useful when one choice is common but we still want callers to be able to choose something different.

## Scene 6 — Local variables and small tests

**Visual:** Show a local variable inside a function. Highlight that the caller uses the returned result, not the internal variable.

**Code**
```python
def average_score(scores):
    total = sum(scores)
    return total / len(scores)

average = average_score([12, 18, 30])
print(average)
```

**Expected output**
```text
20.0
```

**Narration:**

The variable total is created inside the function. It is an implementation detail used to calculate the result. The caller receives the returned average.

Variables created inside a function normally belong to that function. Keeping internal details inside the function helps separate how the calculation works from how the rest of the program uses the answer.

Before trusting a function on a large dataset, test it with small examples. Try a list with one value. Then ask what should happen for an empty list. In this average function, an empty list would lead to division by zero, so a real program needs a deliberate rule for that edge case.

## Scene 7 — Break a large problem into smaller questions

**Visual:** Display four example function names as separate cards or editor lines. Do not implement the complete gradebook or capstone solution.

**Code**
```python
average_score(records)
top_scorer(records)
passed(records, cutoff=70)
grade_map(records)
```

**Narration:**

A larger program can be divided into functions that answer smaller questions.

One function might calculate an average. Another might find the top scorer. Another might determine who passed using a cutoff. Another might map records to grades.

We haven't implemented those examples here. They're examples of how to name the smaller jobs inside a bigger program.

This process is called decomposition. When a program feels too large, ask what smaller questions it needs to answer. Give each clear task a name, and then combine the results.

## Scene 8 — Recap

**Visual:** Reveal: define, call, parameter, argument, return, default, local variable, decomposition.

**Narration:**

Let's recap.

Defining a function creates a reusable block of logic. Calling it runs the function. Parameters are the named inputs in the definition, and arguments are the values supplied in a call.

Print displays a result. Return gives a value back so the caller can use it. A default parameter provides a value when the caller doesn't supply one. Local variables help keep internal details inside a function.

And remember: breaking a large task into small, clearly named functions is a problem-solving skill.

## Final call to action — watch the practice video

**Visual:** Use a neutral end card reading “Next: Practice Video”. Do not show or describe unfinished PyLearn app screens.

**Narration:**

Great work! You've finished this lesson. The next step is to watch the practice video. I recommend watching it because it will help you apply what you've learned with a fresh example.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

**Visual:** Hold the “Next: Practice Video” end card long enough to read.

## Production and QA checklist

- [ ] Verify the exact approved Kendrick voice ID before generating audio.
- [ ] Use ElevenLabs v3 and the same approved voice identity throughout.
- [ ] Keep headings and visual directions out of spoken narration.
- [ ] Verify every code sample and output in Python.
- [ ] Make parameter, argument, and return behavior visually clear.
- [ ] Do not reveal the required Lesson 10 exercise solution or a full capstone solution.
- [ ] Preserve the required PyLearn navigation ending and progression rule.
