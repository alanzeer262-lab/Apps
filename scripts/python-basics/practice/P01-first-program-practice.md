# PyLearn Guided Practice 01 — First Program

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
 > - Voice setup: user confirmed the approved Kendrick / ElevenLabs v3 setup is settled; use the existing configured voice without substitution.
> - No guessed ID, substitution, or preset; use the same approved voice identity throughout.
> - Speak narration only; do not read scene headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/01-first-program.md`, branch `ccr-c7f6fdd7-xpzi3g`.
**Target runtime:** Approximately 2–4 minutes.
**Purpose:** Separate guided-practice companion using fresh examples; never reveal the required app exercise solution.

## Scene 1 — Try a fresh message

**Visual:** Empty editor, same visual design as the lesson video.

**Narration:** Let's practice with a new example. We'll write a message, run it, and check what appears. Type this line:

```python
print("Welcome to my study desk!")
```

Before running it, predict the exact message. Now run it.

**Expected output**
```text
Welcome to my study desk!
```

**Narration:** The text inside the quotation marks is displayed exactly as written. The quotes tell Python that this is a string; the quote marks themselves do not appear in the output.

## Scene 2 — Print a calculation

**Visual:** Add a second line below the first.

**Code**
```python
print(4 + 6)
```

**Expected output:** `10`

**Narration:** The plus sign is outside quotation marks, so Python calculates four plus six. Predict first, then run it. Now change one number and predict again.

## Scene 3 — Add a comment

**Code**
```python
# My first practice note
print("Ready to learn")
```

**Expected output**
```text
Ready to learn
```

**Narration:** The line beginning with the hash symbol is a comment. Python ignores it when running the program. Comments are for people reading the code.

## Scene 4 — Repair a small mistake

**Visual:** Show the broken line first and run it separately. Then replace it with the corrected line and run again. Do not leave the broken and corrected versions in the same runnable code block.

**Broken code — expected SyntaxError**
```python
print("Hello)
```

**Corrected code**
```python
print("Hello")
```

**Expected output**
```text
Hello
```

**Narration:** This line has a missing closing quotation mark. Python can't tell where the string ends, so it reports a syntax error. Add the matching quote, run the corrected line, and check the result. Change one thing at a time when debugging.

## Close — Complete the exercise

**Visual:** Use a simple end card: “Your turn: Complete the exercise”. Do not show or describe unfinished PyLearn app screens.

**Narration:** Great job! Now it's your turn. Complete the exercise to unlock the next lesson. If you'd like more hands-on practice, you can also try the practice in the PyLearn app. Keep going!

## Production checklist
- [x] Approved Kendrick / ElevenLabs v3 voice setup confirmed by the user; use the existing configuration without substitution.
- [ ] Use ElevenLabs v3 with the same approved voice identity.
- [ ] Verify all code and outputs in Python.
- [ ] Keep code and output synchronized with narration.
- [ ] Do not reveal the required app exercise solution.
- [ ] End by directing the learner to the required PyLearn exercise.
