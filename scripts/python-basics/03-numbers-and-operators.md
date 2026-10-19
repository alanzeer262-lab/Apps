# PyLearn Video 03 — Numbers and Operators

**Voice lock — mandatory:** Kendrick voice; ElevenLabs v3; use the exact approved Kendrick voice ID; no substitution or preset; same voice throughout.
**Source:** `Pylearn-build260/content/python-basics/modules/03-numbers-operators.md`
**Target:** 6–8 minutes. Video complements the app lesson; do not change app content.

## Learning outcome
Use arithmetic, division, floor division, remainder, powers, rounding, precedence, and units to build a small study-time report.

## Narration and visual plan

### Scene 1 — A useful question
**Visual:** Dark editor. Type `minutes = 360`, then `hours = minutes / 60`, then `print(hours)`. Run only after the narration asks for a prediction.
**Narration:** “Imagine you studied for 360 minutes this week. How many hours is that? We could calculate it ourselves, but Python can do the arithmetic reliably. First, we store the minutes in a variable. Then we divide by 60, because an hour contains 60 minutes. Before we run it, predict the result.”
**Output:** `6.0`.
**Narration:** “Python gives us 6.0. Normal division keeps a fractional result, even when this answer is a whole number.”

### Scene 2 — The familiar operators
**Visual:** Reveal `10 + 3`, `10 - 3`, `10 * 3`, `10 / 3` one at a time; run as a compact block.
**Narration:** “Addition, subtraction, multiplication, and division use the operators you already know: plus, minus, star, and slash. Let's focus on two operators that answer different questions.”

### Scene 3 — Whole groups and what remains
**Visual:** `print(10 // 3)` then `print(10 % 3)`; show output 3 and 1 separately.
**Narration:** “Floor division, written with two slashes, tells us how many complete groups fit. Ten divided into groups of three gives three complete groups. The remainder operator, percent, tells us what is left over: one. These work together for time.”
**Visual:** Type `minutes = 187`, `hours = minutes // 60`, `remaining_minutes = minutes % 60`; reveal outputs 3 and 7.
**Narration:** “187 minutes is three complete hours and seven minutes remaining. Notice that the operators were chosen because of what we wanted to know.”

### Scene 4 — Powers, rounding, and order
**Visual:** Show `print(2 ** 3)` → `8`; then `print(round(79.8333333333, 2))` → `79.83`.
**Narration:** “Two stars mean a power. Two to the power of three is two multiplied by itself three times, which gives eight. When a decimal has too many digits, round can keep the number of decimal places you choose. Here, two means two decimal places.”
**Visual:** Show `10 + 2 * 3` → 16, then `(10 + 2) * 3` → 36.
**Narration:** “Python follows mathematical precedence: multiplication happens before addition. Parentheses change the order. Without parentheses, this result is sixteen. With parentheses around ten plus two, the result is thirty-six. Use parentheses whenever they make your intention clearer.”

### Scene 5 — Track the units
**Visual:** Build `weekly_minutes = 425`, `weekly_hours = weekly_minutes / 60`, `monthly_hours = weekly_minutes * 4 / 60`.
**Narration:** “A calculation can be syntactically correct and still answer the wrong question. Here, the variable contains minutes. Dividing by sixty converts minutes to hours. Multiplying by four estimates four weeks. Always ask: what does this number represent—minutes, hours, money, items, or scores?”
**Visual:** Add readable print lines with f-strings; run and show actual output.

### Scene 6 — Prediction and practice
**Narration:** “Pause and predict: if weekly minutes changes from 425 to 500, which results change? Take a few seconds.”
**Visual:** Hold only the relevant code for 4 seconds; then run and reveal.
**Narration:** “Now build your own report. Show decimal hours, complete hours, remaining minutes, and estimated monthly hours rounded to one decimal place. Change the input and check your prediction.”

### Recap
**Narration:** “Today you used arithmetic, floor division for complete groups, remainder for what is left, powers, rounding, and parentheses. Most importantly, you learned to check the meaning and units of a result. Next, we'll work with text using strings and f-strings.”
