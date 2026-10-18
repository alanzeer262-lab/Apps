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
  intentionalError?: boolean;
};

const scale = 411.768 / 435;

export const lesson = {
  title: "Your First Python Program",
  subtitle: "Write it. Run it. Understand it.",
  lessonLabel: "PYTHON BASICS  •  LESSON 01",
  durationSeconds: 411.768,
  fps: 30,
  // Add the supplied MP3s to public/audio/ with these exact names.
  narration: [
    { src: "/audio/PyLearn_Video_01_Narration_Part_1.mp3", start: 0 },
    { src: "/audio/PyLearn_Video_01_Narration_Part_2.mp3", start: 173.871 },
  ],
  scenes: [
    { id: 1, title: "Your first conversation", start: 0, end: 48, code: ['print("Hello, I\'m Python.")'], output: ["Hello, I'm Python."], caption: "Write a line. Run it. Observe what happens.", status: "PROGRAM COMPLETE" },
    { id: 2, title: "Python can calculate", start: 48, end: 85, code: ['print("Hello!")', "print(2 + 3)"], output: ["Hello!", "5"], prompt: "What do you predict?", caption: "print() can display text and calculation results.", status: "OUTPUT REVEALED" },
    { id: 3, title: "Two values that look alike", start: 85, end: 120, code: ["print(10)", 'print("10")'], output: ["10", "10"], prompt: "Will these behave the same?", caption: "The output looks alike, but one value is a number and one is text.", status: "COMPARE VALUES" },
    { id: 4, title: "Strings and quote errors", start: 120, end: 162, code: ['name = "Ada"', 'message = "Python is fun"', "", 'print("Hello")', "print('Hello')"], output: ["Hello", "Hello"], prompt: "Intentional error example: print(\"Hello)", caption: "Matching quotation marks keep strings valid.", status: "VALID EXAMPLE" },
    { id: 5, title: "A note for humans", start: 162, end: 192, code: ["# This line explains the program", 'print("The code still runs.")'], output: ["The code still runs."], caption: "Comments start with # and do not appear in program output.", status: "OUTPUT REVEALED" },
    { id: 6, title: "Make it personal with f-strings", start: 192, end: 248, code: ['name = "Ada"', 'goal = "Data Analyst"', "", 'print(f"My name is {name}.")', 'print(f"My goal is to become a {goal}.")'], output: ["My name is Ada.", "My goal is to become a Data Analyst."], prompt: "Change Ada to Sam and run it again.", caption: "Curly braces insert variable values into an f-string.", status: "PERSONALIZED OUTPUT" },
    { id: 7, title: "Showing versus returning", start: 248, end: 345, code: ["def show_total(bill):", "    print(bill + 10)", "", "def add_tip(bill):", "    return bill + 10", "", "total = add_tip(40)", 'print(f"You pay: {total}")', 'print(f"For a table of two: {total * 2}")'], output: ["You pay: 50", "For a table of two: 100"], prompt: "print shows a value; return hands it back.", caption: "Returned values can be stored and reused. A function without return gives None.", status: "VALUE RETURNED" },
    { id: 8, title: "A calm approach to debugging", start: 345, end: 377, code: ['print("Welcome to Python")'], output: ["Welcome to Python"], prompt: "Read the error. Check the line. Change one thing.", caption: "Fix one issue at a time, then run the program again.", status: "ERROR FIXED" },
    { id: 9, title: "Your turn", start: 377, end: 408, code: ['name = "Your name"', 'goal = "Your learning goal"', "hours = 0  # weekly study hours", "", "# Add three friendly f-string messages"], output: [], prompt: "Build your own introduction. Predict before you run.", caption: "Your task: introduce yourself using variables and f-strings.", status: "YOUR TURN" },
    { id: 10, title: "Connect today's ideas", start: 408, end: 435, code: ['print("Hello!")', 'message = "Python is fun"  # a string', 'print(f"Hello, {name}!")', "# print shows; return hands a value back"], output: ["Your First Python Program — Complete", "Next: Variables and Data Types"], caption: "You have the foundations. Next: variables and data types.", status: "LESSON COMPLETE" },
  ].map((scene) => ({ ...scene, start: scene.start * scale, end: scene.end * scale })) as LessonScene[],
};

export const narrationDurationSeconds = 411.768;
