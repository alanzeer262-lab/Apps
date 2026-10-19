# PyLearn Video 13 — Build: Study Time Calculator

**Voice lock — mandatory:** Kendrick; ElevenLabs v3; exact approved Kendrick voice ID; no substitution/preset; same voice throughout.
**Source:** `Pylearn-build260/content/python-basics/modules/13-build-study-calculator.md`
**Target:** 5–7 minutes.

### Scene 1 — Define the job
**Visual:** Show input example 360 minutes, 6 sessions; label outputs: total minutes, full hours, remaining minutes, average session length.
**Narration:** “Our next project is a study-time calculator. It takes total minutes and the number of sessions, then reports the total, complete hours, remaining minutes, and average length per session. We'll use the operators because each answers a different question.”

### Scene 2 — Build the function
**Visual:** Type `def study_time_report(total_minutes, sessions):` and calculate `full_hours = total_minutes // 60`, `remaining_minutes = total_minutes % 60`, `average_session = total_minutes / sessions`.
**Narration:** “Floor division gives complete hours. Modulo gives the remaining minutes. Normal division calculates the average session length. Rounding can make the average easier to read. The names also remind us what units each number represents.”

### Scene 3 — Handle zero sessions
**Visual:** Before division, show a conditional for `sessions == 0` returning `"No study sessions recorded."`.
**Narration:** “What if no sessions were recorded? Dividing by zero would fail, and the report should not pretend an average exists. We handle that case first and return the message specified by the project.”
**Visual:** Run zero-session case and show message.

### Scene 4 — Verify examples
**Visual:** Run 360 minutes over 6 sessions, then 65 minutes over 2 sessions. Show each output and units.
**Narration:** “For 360 minutes over six sessions, check the total and average. Then test sixty-five minutes over two sessions. Do not just check that the program runs—check that the result answers the question and uses the correct units.”

### Scene 5 — Practice
**Narration:** “Your turn. Add another test with a different number of minutes. Predict the complete hours, remainder, and average before running. Then explain why floor division is useful here when normal division is also available.”
**Hold:** 4 seconds.
**Narration:** “You built a calculator that combines arithmetic, units, functions, and an explicit edge-case rule. Next, we'll clean inconsistent topic text.”
