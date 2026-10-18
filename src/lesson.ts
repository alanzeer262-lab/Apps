export type Caption = { start: number; end: number; text: string };

export const lesson = {
  title: "Your First Python Program",
  subtitle: "Make the computer speak",
  lessonLabel: "PYTHON BASICS  •  LESSON 01",
  code: ['print("Hello, world!")'],
  output: ["Hello, world!"],
  // Place the narration file in public/audio and update this path.
  audioSrc: undefined as string | undefined,
  durationSeconds: 18,
  captions: [
    { start: 0.5, end: 3.4, text: "Every Python journey starts with one simple instruction." },
    { start: 3.5, end: 7.2, text: "The print function displays a message on the screen." },
    { start: 7.3, end: 11.8, text: "Put your message inside quotation marks." },
    { start: 11.9, end: 16.5, text: "Run the program, and Python prints: Hello, world!" },
  ] as Caption[],
};
