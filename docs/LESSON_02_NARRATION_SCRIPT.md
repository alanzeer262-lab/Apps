# PyLearn Video 02 — Narration Script
**Source of truth:** `content/python-basics/modules/02-variables-types.md` in `Pylearn-build260`, branch `ccr-c7f6fdd7-xpzi3g`.
**Purpose:** Spoken narration for recording. Bracketed directions are production notes and should not be read aloud.
**Target:** Approximately 7–8 minutes at a calm teaching pace, including pauses.

---

## Scene 1 — A program needs to remember information

A useful program needs to remember information.

Imagine we're building a small learner profile. We need to keep the learner's name, how many hours they study, and their goal. We need somewhere to store each of those values so the program can use them later.

In Python, we can give each value a name. Those names are called variables.

For example, we could write:

```python
name = "Ada"
hours = 6
goal = "Data Analyst"
```

[Reveal the three assignments one at a time.]

You can think of a variable as a label attached to a value. The name helps us refer to that value without typing it again every time.

Let's look at how assignment works.

## Scene 2 — Assigning and changing a value

Start with these two lines:

```python
name = "Ada"
print(name)
```

[Run the code. Expected output: Ada.]

The output is Ada. Notice that the word name in the print statement has no quotation marks. We're asking Python to look up the value associated with the variable named name.

Now let's change the value.

```python
name = "Sam"
print(name)
```

[Run the code. Expected output: Sam.]

The output is now Sam. We can also write both assignments one after the other:

```python
name = "Ada"
name = "Sam"
print(name)
```

[Run the code. Expected output: Sam.]

Python prints Sam because the second assignment replaces the value previously assigned to name.

The equals sign here means assignment. Python takes the value on the right and stores it under the name on the left. It's not a claim that the two sides are mathematically equal.

This is useful because we can change a value in one place and have the program use the new value wherever that variable is read.

## Scene 3 — Values have different types

Variables can store different kinds of values. Python calls these kinds types.

Look at these four examples:

```python
name = "Ada"
age = 36
price = 19.99
is_student = True
```

[Highlight each line as it is named.]

The first value is text inside quotation marks. Its type is called a string, or str.

The value thirty-six is a whole number. Its type is an integer, or int.

The price has a decimal point. Its type is called a float.

And is_student has the value True. That is a Boolean, or bool. Booleans represent true or false. In Python, write True and False with capital letters.

So remember these four common types: str for text, int for whole numbers, float for decimal numbers, and bool for true-or-false values.

How can we check a type rather than guessing?

## Scene 4 — Ask Python with type()

Python has a built-in tool called type(). It tells us what type a value has.

Let's ask Python about each of our variables:

```python
print(type(name))
print(type(age))
print(type(price))
print(type(is_student))
```

[Run the code and reveal the output line by line.]

Python reports str, int, float, and bool inside its type results. Those results match the values we assigned.

You won't need to use type() every time you write a program. But when a calculation behaves strangely, checking the type is a useful debugging habit. Instead of guessing, ask: what type is this value?

The type matters because the same-looking characters can behave differently depending on whether Python sees them as a number or as text.

## Scene 5 — The same characters, different behavior

Compare these two lines:

```python
print(21 * 2)
print("21" * 2)
```

[Pause briefly before running. Then show the exact output.]

The first result is forty-two. The second result is twenty-one twenty-one, with the text repeated twice.

Why are the results different?

In the first line, twenty-one is an integer, so the asterisk means multiplication.

In the second line, quotation marks make twenty-one a string. When Python multiplies a string by two, it repeats the text twice.

The characters look similar, but their types are different. This is why checking a type can help explain a result that surprises you.

## Scene 6 — Convert a value when its meaning changes

Sometimes a number arrives as text. For example:

```python
age_text = "21"
```

Right now, age_text is a string. If we want to do arithmetic with that value, we can convert it to an integer using int():

```python
age_text = "21"
age = int(age_text)
print(age + 1)
```

[Run the code. Expected output: 22.]

Python converts the text "21" to the integer 21, so adding one produces 22.

We can convert other values too. For example, float() can convert the text "19.99" to a decimal number, and str() can convert the number 95 to text:

```python
price = float("19.99")
score_text = str(95)
```

But conversion is not magic. Python can only convert a value when its contents are suitable for that type.

For example:

```python
score = int("hello")
```

This fails because the word hello is not a valid integer. Python raises an error instead of guessing what number we meant.

That error gives us useful information. Real programs need to think about invalid input and decide how to handle it safely. We'll build on that idea later.

## Scene 7 — Choose names that explain the code

Variable names should help a person understand the program.

Look at these three assignments:

```python
x = 19.99
p = 19.99
price = 19.99
```

All three names are allowed. But price gives us a clue about what the value means. Names like x and p may force us to remember extra information.

Prefer clear names such as:

```python
customer_name = "Ada"
item_price = 19.99
items_count = 3
```

When a name contains more than one word, Python programmers commonly use snake_case: write the words in lowercase and separate them with underscores.

Good names make code easier to read. They also reduce mistakes because you don't have to remember what every short, unclear name stands for.

## Scene 8 — Predict, then investigate

Now let's test what we've learned. Look at this code:

```python
value = "25"

print(value)
print(type(value))

number = int(value)

print(number)
print(type(number))
print(number * 2)
```

[Show the complete code. Ask the questions before running it. Pause for four seconds.]

Before running it, predict three things.

First, what type is value?

Second, after the conversion, what type is number?

And third, what will the final line print?

[Run the code. Expected output:
25
<class 'str'>
25
<class 'int'>
50.]

The first type is str because value contains text in quotation marks. After int(value), number is an integer. And multiplying that integer by two produces fifty.

If your prediction was different, that's useful. You've found something to investigate. Learning programming isn't about never making a mistake. It's about making a prediction, testing it, and improving your understanding.

## Scene 9 — Your turn: build a learner profile

Now it's your turn to practice.

Create a learner profile with these values:

```python
name = "Ada"
age = 25
study_hours = "6"
is_beginner = True
```

First, inspect the types of the four variables using type().

Next, convert study_hours to an integer. Then calculate study_hours multiplied by four, and print a readable sentence that uses the learner's name and the calculated result.

[Give the learner time to pause and try the task. Do not display a completed solution in the video.]

Now try one small experiment. Change the text "6" to "eight", then try converting it to an integer again.

What happens? The conversion fails because eight is not written as digits that form an integer. This is a useful reminder that real data isn't always in the format a program expects.

## Recap and close

Let's recap.

A variable is a name we use to refer to a value. Assignment stores a value under that name, and a later assignment can replace the earlier value.

Python values have types. Strings are text, integers are whole numbers, floats are decimal numbers, and Booleans represent true or false. The type() function helps us inspect a value.

Types affect what Python does. The number 21 multiplied by two gives 42, while the string "21" multiplied by two repeats the text. When we need a different type, functions such as int(), float(), and str() can convert suitable values.

Finally, choose variable names that explain what the values mean. Clear names make your programs easier to understand and maintain.

You don't need to master everything at once. Practice changing a value, predicting what will happen, running the code, and checking the result.

In the next lesson, we'll continue with numbers and operators. Nice work!
