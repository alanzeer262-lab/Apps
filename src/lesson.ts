export type LessonScene = {
  id: number;
  title: string;
  start: number;
  end: number;
  code: string[];
  output: string[];
  prompt?: string;
  caption: string;
  status: string;
};

const scale = 411.768 / 435;

export const lesson = {
  title: "Your First Python Program",
  subtitle: "Write it. Run it. Understand it.",
  lessonLabel: "PYTHON BASICS  •  LESSON 01",
  durationSeconds: 411.768,
  fps: 30,
  // Copy the two supplied narration MP3s into public/audio/ before rendering.
  narration: [
    { src: "/audio/PyLearn_Video_01_Narration_Part_1.mp3", start: 0 },
    { src: "/audio/PyLearn_Video_01_Narration_Part_2.mp3", start: 173.871 },
  ],
  // Times below follow the storyboard's 7:15 structure and are scaled to the
  // measured narration length (6:51.768), preserving the original audio speed.
  scenes: [
    { id: 1, title: "Your first conversation", start: 0, end: 48, code: ['print("Hello, I\'m Python.")'], output: ["Hello, I'm Python."], caption: "Write a line. Run it. Observe what happens.", status: "PROGRAM COMPLETE" },
    { id: 2, title: "Python can calculate", start: 48, end: 85, code: ['print("Hello!")', "print(2 + 3)"], output: ["Hello!", "5"], prompt: "What do you predict?", caption: "print() can display text and calculation results.", status: "OUTPUT REVEALED" },
    { id: 3, title: "Two values that look alike", start: 85, end: 120, code: ["print(10)", 'print("10")'], output: ["10", "10"], prompt: "Will these behave the same?", caption: "The output looks alike, but one value is a number and one is text.", status: "COMPARE VALUES" },
    { id: 4, title: "Matching quotation marks", start: 120, end: 162, code: ['name = "Ada"', 'message = "Python is fun"', "", 'print("Hello")', "print('Hello')"], output: ["Hello", "Hello"], prompt: "Scratch example: print(\"Hello)", caption: "Python reports a syntax error when a string's closing quote is missing.", status: "CHECK THE QUOTES" },
    { id: 5, title: "A note for humans", start: 162, end: 192, code: ["# This line explains the program", 'print("The code still runs.")'], output: ["The code still runs."], caption: "Comments start with # and do not appear in program output.", status: "OUTPUT REVEALED" },
    { id: 6, title: "Make the message personal", start: 192, end: 213, code: ['name = "Ada"', 'goal = "Data Analyst"', "", 'print(f"My name is {name}.")', 'print(f"My goal is to become a {goal}.")'], output: ["My name is Ada.", "My goal is to become a Data Analyst."], prompt: "Notice the f prefix and curly braces.", caption: "F-strings insert variable values into readable messages.", status: "PERSONALIZED OUTPUT" },
    { id: 7, title: "Change one value", start: 213, end: 230, code: ['name = "Sam"', 'goal = "Data Analyst"', "", 'print(f"My name is {name}.")', 'print(f"My goal is to become a {goal}.")'], output: ["My name is Sam.", "My goal is to become a Data Analyst."], prompt: "Only the name changed.", caption: "Update a variable and the message changes automatically.", status: "VALUE UPDATED" },
    { id: 8, title: "Include a number in a message", start: 230, end: 248, code: ["hours = 6", 'print(f"I study {hours} hours each week.")'], output: ["I study 6 hours each week."], caption: "F-strings can include numbers as well as text.", status: "OUTPUT REVEALED" },
    { id: 9, title: "Define two functions", start: 248, end: 278, code: ["def show_total(bill):", "    print(bill + 10)", "", "def add_tip(bill):", "    return bill + 10"], output: [], prompt: "Definitions create recipes; they do not run yet.", caption: "Defining a function does not execute its body.", status: "FUNCTIONS DEFINED" },
    { id: 10, title: "Return a value and reuse it", start: 278, end: 310, code: ["total = add_tip(40)", 'print(f"You pay: {total}")', 'print(f"For a table of two: {total * 2}")'], output: ["You pay: 50", "For a table of two: 100"], prompt: "The returned total can be reused.", caption: "return hands the result back so the program can use it again.", status: "VALUE RETURNED" },
    { id: 11, title: "print versus return", start: 310, end: 345, code: ["saved = show_total(40)", "print(saved)"], output: ["50", "None"], prompt: "The function prints 50 but returns None.", caption: "print shows a value; return hands a value back to the rest of the code.", status: "COMPARE RESULTS" },
    { id: 12, title: "A calm approach to debugging", start: 345, end: 377, code: ['print("Welcome to Python")'], output: ["Welcome to Python"], prompt: "Fix: add the missing closing quote, then run again.", caption: "Read the error. Check the line. Change one thing. Run again.", status: "ERROR FIXED" },
    { id: 13, title: "Your turn", start: 377, end: 408, code: ['name = "Your name"', 'goal = "Your learning goal"', "hours = 0  # weekly study hours", "", "# Add three friendly f-string messages"], output: [], prompt: "Build your own introduction. Predict before you run.", caption: "Use variables and f-strings to introduce yourself.", status: "YOUR TURN" },
    { id: 14, title: "Connect today's ideas", start: 408, end: 435, code: ['print("Hello!")', 'message = "Python is fun"  # a string', 'print(f"Hello, {name}!")', "# print shows; return hands a value back"], output: ["Your First Python Program — Complete", "Next: Variables and Data Types"], caption: "You have the foundations. Next: variables and data types.", status: "LESSON COMPLETE" },
  ].map((scene) => ({ ...scene, start: scene.start * scale, end: scene.end * scale })) as LessonScene[],
};

export const narrationDurationSeconds = 411.768;
