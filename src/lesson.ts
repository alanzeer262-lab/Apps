import alignmentJson from "./generated-alignment.json";

type GeneratedScene = {
  id: number; title: string; caption: string; status: string;
  start: number; end: number; transcriptTopicMatch?: number;
  code: string[]; output: string[]; prompt?: string | null;
  errorCode?: string[] | null; errorOutput?: string[] | null; errorPrompt?: string | null;
  correctedCode?: string[] | null;
};
const generatedAlignment = alignmentJson as {
  generated: boolean; durationSeconds: number; part2StartSeconds: number;
  audioTracks?: { src: string; start: number }[];
  scenes: GeneratedScene[];
};
export type LessonScene = GeneratedScene & {
  codeAt?: number; outputAt?: number; fixAt?: number; errorAt?: number;
};
if (!generatedAlignment.generated) {
  throw new Error("Transcript-derived scene manifest is missing. Run scripts/align_narration.py before rendering.");
}
if (!generatedAlignment.scenes.length) {
  throw new Error("Transcript-derived scene manifest contains no scenes. Refusing to render.");
}
export const lesson = {
  title: "Your First Python Program",
  subtitle: "Write it. Run it. Understand it.",
  lessonLabel: "PYTHON BASICS  •  LESSON 01",
  durationSeconds: generatedAlignment.durationSeconds,
  fps: 30,
  narration: generatedAlignment.audioTracks ?? [
    { src: "/audio/lesson-01/part-01.mp3", start: 0 },
    { src: "/audio/lesson-01/part-02.mp3", start: generatedAlignment.part2StartSeconds },
  ],
  scenes: generatedAlignment.scenes as LessonScene[],
};
export const narrationDurationSeconds = lesson.durationSeconds;
