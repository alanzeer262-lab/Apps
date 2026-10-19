A function that reads a file and calculates an average in one block has two responsibilities. Imagine separating file loading from average calculation.

When a function lives in a module, another file can import it rather than copying its implementation. Keep the interface small and predictable.

Use this example to decide which code belongs in a reusable calculation module and which belongs in the report layer.

Good work. Now complete the exercise to unlock the next lesson. Use the habits from this practice: test small cases, check assumptions, and change one thing at a time. If you'd like extra hands-on practice, you can also try it in the PyLearn app.
