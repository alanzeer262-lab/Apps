# PyLearn Video 13 — Build: Study Time Calculator

**Voice lock:** Kendrick · ElevenLabs v3 · exact user-approved Kendrick voice ID only; no preset or substitution.
**Canonical source:** app Module 13, Build 2. **Target:** 3–4 minutes. Teach the ideas; do not show the complete project solution.

## Scene 1 — The mission
**Visual:** Show input labels: total minutes and number of sessions. Show required output labels: total minutes, full hours, remaining minutes, average session length.
**Narration:** “This project turns study time into a useful report. You'll give it total minutes and the number of sessions. It must report the total, complete hours, remaining minutes, and average session length.”

## Scene 2 — Three operators, three jobs
**Visual:** Reveal the expressions one at a time, without assembling the function: `total_minutes / sessions`, `total_minutes // 60`, `total_minutes % 60`.
**Narration:** “Normal division can calculate an average. Floor division by sixty gives complete hours. Modulo by sixty gives the minutes left over. These operators are related, but they answer different questions. Keep the units clear as you work.”

## Scene 3 — Predict
**Visual:** Show **360 minutes** and **6 sessions**. Hide all computed outputs.
**Narration:** “Before running anything, predict the complete hours, the remaining minutes, and the average length of one session. Which operation answers each question?”
**Hold:** 5 seconds of silence. Reveal the three answers only after the pause: 6 full hours, 0 remaining minutes, 60 minutes per session.

## Scene 4 — A necessary edge case
**Visual:** Show `sessions = 0`; highlight the required message: “No study sessions recorded.”
**Narration:** “The app's project brief defines one special case: if sessions is zero, return the message ‘No study sessions recorded.’ You must check this before dividing, because division by zero fails.”

## Scene 5 — Build it in PyLearn
**Visual:** App/project card: **Build 2 — Study time calculator**. Tests listed: 360 minutes / 6 sessions; 65 minutes / 2 sessions; 0 sessions.
**Narration:** “Open Build 2 in PyLearn and write study_time_report yourself. Test all three cases, including zero sessions. Then explain in your own words why floor division is useful when normal division is also available.”

## Final call to action — required for YouTube and in-app versions

**Visual:** Show the PyLearn app's Practice section and the matching project card: **Build 2 — Study time calculator**. Do not show the completed solution.

**Narration:**

Now it's your turn to build it yourself.

Open the PyLearn app and go to the Practice section for this project. If you're watching on YouTube, open PyLearn and find Build 2 — Study time calculator in the app.

Write the code yourself, run it, and use the app's feedback to check your work. Try the required cases before moving on. Mistakes are part of learning, so read the feedback and try again.

Watching the example is only the first step. Now open PyLearn and build it yourself!

**End card:** “Open PyLearn → Practice → Build 2 — Study time calculator”

## Production checklist

- [ ] The video demonstrates the problem and reasoning without giving away the complete app solution.
- [ ] The final card explicitly points to Practice in PyLearn.
- [ ] YouTube viewers are told to open PyLearn and find the matching project.
- [ ] Review the full rendered video at normal speed before marking it complete.
