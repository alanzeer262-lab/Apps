Now we move from individual skills to a small toolkit. The loader's job is narrow: take raw C S V text and turn it into a consistent list of records. It should not calculate averages or decide which scores are valid.

The input is plain text. A loader parses the rows and trims stray spaces so later functions receive predictable values.

For this demonstration, we'll use Python's C S V reader with an in-memory text stream. That lets us show the parsing idea without needing a real file on screen.

The C S V reader recognizes the header fields. At this stage, the score is still text. Loading should preserve the parsed value and leave validation to the next step.

Real inputs may have extra spaces or a final blank line. A good loader trims fields and skips rows that contain no meaningful data. That makes its output more consistent without hiding invalid scores.

Trimming whitespace is not the same as deciding whether a score is valid. Keep the loader's job focused, then test its behavior on clean rows and awkward formatting.

Great work! You've finished Build: Load a Scores C S V. Next, watch the practice video. I recommend watching it because we'll use a fresh example to reinforce the skill from this lesson.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.
