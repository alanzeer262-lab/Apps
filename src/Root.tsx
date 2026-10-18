import React from "react";
import { Composition } from "remotion";
import { PyLearnVideo } from "./Video";
import { lesson } from "./lesson";
import lesson02Json from "./lesson-02.json";

const FPS = 30;
const lesson02 = lesson02Json as typeof lesson;

export const RemotionRoot: React.FC = () => (
  <>
    <Composition
      id="PyLearnLesson"
      component={PyLearnVideo}
      durationInFrames={Math.ceil(lesson.durationSeconds * FPS)}
      fps={FPS}
      width={1920}
      height={1080}
    />
    <Composition
      id="PyLearnLesson02"
      component={PyLearnVideo}
      defaultProps={{ lessonData: lesson02 }}
      durationInFrames={Math.ceil(lesson02.durationSeconds * FPS)}
      fps={FPS}
      width={1920}
      height={1080}
    />
  </>
);
