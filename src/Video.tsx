import React from "react";
import { AbsoluteFill, Audio, interpolate, Sequence, useCurrentFrame, useVideoConfig } from "remotion";
import { lesson } from "./lesson";
import "./styles.css";

const colors = { bg: "#08111f", panel: "#101d30", border: "#24364f", text: "#f4f7fb", muted: "#9fb0c7", cyan: "#5eead4", yellow: "#fbbf24", green: "#86efac" };

export const PyLearnVideo: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const titleY = interpolate(frame, [0, 20], [36, 0], { extrapolateRight: "clamp" });
  const titleOpacity = interpolate(frame, [0, 18], [0, 1], { extrapolateRight: "clamp" });
  const codeProgress = interpolate(frame, [18, 58], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const outputOpacity = interpolate(frame, [72, 88], [0, 1], { extrapolateRight: "clamp" });
  const activeCaption = lesson.captions.find(c => frame / fps >= c.start && frame / fps < c.end);

  return (
    <AbsoluteFill style={{ background: colors.bg, color: colors.text, fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif", padding: 76, overflow: "hidden" }}>
      {lesson.audioSrc ? <Audio src={lesson.audioSrc} /> : null}
      <div className="glow glow-one" /><div className="glow glow-two" />
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", zIndex: 1 }}>
        <div className="brand"><span className="brand-mark">Py</span><span>PyLearn</span></div>
        <div className="lesson-label">{lesson.lessonLabel}</div>
      </div>

      <div style={{ marginTop: 66, opacity: titleOpacity, transform: `translateY(${titleY}px)`, zIndex: 1 }}>
        <div className="eyebrow">LEARN BY DOING</div>
        <h1>{lesson.title}</h1>
        <p className="subtitle">{lesson.subtitle}</p>
      </div>

      <div className="workspace" style={{ zIndex: 1 }}>
        <section className="code-panel">
          <div className="panel-header"><div className="traffic"><i /><i /><i /></div><span>main.py</span><span className="file-type">PYTHON</span></div>
          <div className="code-content">
            <div className="line-number">1</div>
            <div className="code-line">
              <span className="syntax-fn">{lesson.code[0].split("(")[0]}</span><span>(</span><span className="syntax-string">{lesson.code[0].includes('"') ? lesson.code[0].split('"')[1] : lesson.code[0]}</span><span>)</span>
              <span className="typing-caret" style={{ opacity: frame % 30 < 16 && codeProgress < 1 ? 1 : 0 }} />
            </div>
          </div>
          <div className="code-hint"><span className="hint-dot" /> One line. A real Python program.</div>
        </section>

        <section className="output-panel" style={{ opacity: outputOpacity, transform: `translateY(${interpolate(frame, [72, 88], [20, 0], { extrapolateRight: "clamp" })}px)` }}>
          <div className="panel-header"><span className="terminal-icon">›_</span><span>TERMINAL</span><span className="running">● COMPLETE</span></div>
          <div className="output-content"><div className="output-prompt">$ python main.py</div>{lesson.output.map((line, i) => <div className="output-line" key={i}>{line}</div>)}<div className="success-note"><span>✓</span> Program finished successfully</div></div>
        </section>
      </div>

      <div className="bottom-bar" style={{ zIndex: 1 }}>
        <div className="progress-track"><div className="progress-fill" style={{ width: `${Math.min(100, frame / (lesson.durationSeconds * fps) * 100)}%` }} /></div>
        <div className="caption">{activeCaption?.text ?? "A small step. A new skill."}</div>
        <div className="footer-meta"><span>PYTHON FOUNDATIONS</span><span>{String(Math.floor(frame / fps)).padStart(2, "0")} / {lesson.durationSeconds}s</span></div>
      </div>
    </AbsoluteFill>
  );
};
