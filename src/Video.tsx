import React from "react";
import { AbsoluteFill, Audio, Sequence, interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { lesson } from "./lesson";
import "./styles.css";

const colors = { bg: "#08111f", panel: "#101d30", border: "#24364f", text: "#f4f7fb", muted: "#9fb0c7", cyan: "#5eead4", yellow: "#fbbf24", green: "#86efac" };

function syntaxLine(line: string) {
  const parts = line.split(/("[^"]*"|'[^']*'|\\b(?:def|return|print|if|else|for|in|True|False|None)\\b|#[^$]*)/g);
  return parts.map((part, i) => {
    let cls = "";
    if (/^".*"$|^'.*'$/.test(part)) cls = "syntax-string";
    else if (/^#/.test(part)) cls = "syntax-comment";
    else if (/^(def|return|print|if|else|for|in|True|False|None)$/.test(part)) cls = "syntax-fn";
    return <span className={cls} key={i}>{part}</span>;
  });
}

export const PyLearnVideo: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const seconds = frame / fps;
  const scene = lesson.scenes.find((s) => seconds >= s.start && seconds < s.end) ?? lesson.scenes[lesson.scenes.length - 1];
  const localFrame = Math.max(0, frame - Math.round(scene.start * fps));
  const fade = interpolate(localFrame, [0, 12], [0, 1], { extrapolateRight: "clamp" });
  const elapsed = Math.floor(seconds);
  const showOutput = seconds >= scene.start + Math.min(8, (scene.end - scene.start) * 0.22);

  return (
    <AbsoluteFill style={{ background: colors.bg, color: colors.text, fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif", padding: 66, overflow: "hidden" }}>
      {lesson.narration.map((track) => (
        <Sequence key={track.src} from={Math.round(track.start * fps)}>
          <Audio src={track.src} />
        </Sequence>
      ))}
      <div className="glow glow-one" /><div className="glow glow-two" />
      <div className="topbar">
        <div className="brand"><span className="brand-mark">Py</span><span>PyLearn</span></div>
        <div className="lesson-label">{lesson.lessonLabel}</div>
      </div>

      <div className="heading" style={{ opacity: fade }}>
        <div className="eyebrow">LEARN BY DOING · SCENE {String(scene.id).padStart(2, "0")}</div>
        <h1>{scene.title}</h1>
        <p className="subtitle">{lesson.subtitle}</p>
      </div>

      <div className="workspace" style={{ opacity: fade }}>
        <section className="code-panel">
          <div className="panel-header"><div className="traffic"><i /><i /><i /></div><span>main.py</span><span className="file-type">PYTHON</span></div>
          <div className="code-content">
            {scene.code.map((line, i) => (
              <div className="code-row" key={i}>
                <span className="line-number">{String(i + 1).padStart(2, " ")}</span>
                <span className="code-line">{line ? syntaxLine(line) : " "}</span>
              </div>
            ))}
            <div className="typing-caret" style={{ opacity: Math.floor(seconds * 2) % 2 === 0 ? 1 : 0 }} />
          </div>
          <div className="code-hint"><span className="hint-dot" /> Code stays connected as the lesson progresses</div>
        </section>

        <section className="output-panel" style={{ opacity: showOutput ? 1 : 0.5 }}>
          <div className="panel-header"><span className="terminal-icon">›_</span><span>OUTPUT</span><span className="running">● {scene.status}</span></div>
          <div className="output-content">
            {scene.prompt ? <div className="output-prompt">{scene.prompt}</div> : <div className="output-prompt">$ python main.py</div>}
            {scene.output.length ? scene.output.map((line, i) => <div className={scene.id === 10 ? "output-line final-line" : "output-line"} key={i}>{line}</div>) : <div className="waiting">Waiting for your code…</div>}
          </div>
        </section>
      </div>

      <div className="bottom-bar">
        <div className="progress-track"><div className="progress-fill" style={{ width: `${Math.min(100, seconds / lesson.durationSeconds * 100)}%` }} /></div>
        <div className="caption">{scene.caption}</div>
        <div className="footer-meta"><span>PYTHON FOUNDATIONS</span><span>{String(Math.floor(elapsed / 60)).padStart(2, "0")}:{String(elapsed % 60).padStart(2, "0")} / 06:52</span></div>
      </div>
    </AbsoluteFill>
  );
};
