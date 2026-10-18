import React from "react";
import { Composition } from "remotion";
import { PyLearnVideo } from "./Video";
import { lesson } from "./lesson";

const FPS = 30;

export const RemotionRoot: React.FC = () => (
  <Composition
    id="PyLearnLesson"
    component={PyLearnVideo}
    durationInFrames={lesson.durationSeconds * FPS}
    fps={FPS}
    width={1920}
    height={1080}
  />
);
