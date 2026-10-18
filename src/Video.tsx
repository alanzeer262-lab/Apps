import React from "react";
import { AbsoluteFill, Audio, Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { lesson } from "./lesson";
import "./styles.css";

const colors = { bg: "#08111f", panel: "#101d30", border: "#24364f", text: "#f4f7fb", muted: "#9fb0c7", cyan: "#5eead4", yellow: "#fbbf24", green: "#86efac" };

function syntaxLine(line: string) {
  const parts = line.split(/("[^"]*"|'[^']*'|\b(?:def|return|print|if|else|for|in|True|False|None)\b|#[^$]*)/g);
  return parts.map((part, i) => {
    let cls = "";
    if (/^".*"$|^'.*'$/.test(part)) cls = "syntax-string";
    else if (/^#/.test(part)) cls = "syntax-comment";
    else if (/^(def|return|print|if|else|for|in|True|False|None)$/.test(part)) cls = "syntax-fn";
    return <span className={cls} key={i}>{part}</span>;
  });
}

export const PyLearnVideo: React.FC<{ lessonData?: typeof lesson }> = ({ lessonData = lesson }) => {
  if (!lessonData.scenes.length) {
    throw new Error("Transcript-derived scene manifest is missing for Lesson 01. Run scripts/align_narration.py before rendering Lesson 01.");
  }
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const seconds = frame / fps;
  const scene = lessonData.scenes.find((s) => seconds >= s.start && seconds < s.end) ?? lessonData.scenes[lessonData.scenes.length - 1];
  const localFrame = Math.max(0, frame - Math.round(scene.start * fps));
  const fade = interpolate(localFrame, [0, 12], [0, 1], { extrapolateRight: "clamp" });
  const elapsed = Math.floor(seconds);
  const totalSeconds = Math.ceil(lessonData.durationSeconds);
  const durationLabel = `${String(Math.floor(totalSeconds / 60)).padStart(2, "0")}:${String(totalSeconds % 60).padStart(2, "0")}`;
  const showError = scene.errorAt !== undefined && seconds >= scene.errorAt && !(scene.fixAt !== undefined && seconds >= scene.fixAt);
  const showCompletion = scene.completionAt !== undefined && seconds >= scene.completionAt;
  const showOutput = showError || seconds >= (scene.outputAt ?? scene.start);
  const showCode = seconds >= (scene.codeAt ?? scene.start);
  const codeLines = showError && scene.errorCode ? scene.errorCode : scene.correctedCode && scene.fixAt !== undefined && seconds >= scene.fixAt ? scene.correctedCode : scene.code;
  const outputLines = showError && scene.errorOutput ? scene.errorOutput : scene.output;
  const outputPrompt = showError && scene.errorPrompt ? scene.errorPrompt : scene.prompt ?? "$ python main.py";

  return (
    <AbsoluteFill style={{ background: colors.bg, color: colors.text, fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif", padding: 66, overflow: "hidden" }}>
      {lessonData.narration.map((track) => (
        <Sequence key={track.src} from={Math.round(track.start * fps)}>
          <Audio src={staticFile(track.src.replace(/^\//, ""))} />
        </Sequence>
      ))}
      <div className="glow glow-one" /><div className="glow glow-two" />
      <div className="topbar">
        <div className="brand"><span className="brand-mark">Py</span><span>PyLearn</span></div>
        <div className="lesson-label">{lessonData.lessonLabel}</div>
      </div>

      <div className="heading" style={{ opacity: fade }}>
        <div className="eyebrow">LEARN BY DOING · SCENE {String(scene.id).padStart(2, "0")}</div>
        <h1>{scene.title}</h1>
        <p className="subtitle">{lessonData.subtitle}</p>
      </div>

      <div className="workspace" style={{ opacity: fade }}>
        <section className="code-panel">
          <div className="panel-header"><div className="traffic"><i /><i /><i /></div><span>main.py</span><span className="file-type">PYTHON</span></div>
          <div className="code-content">
            {showCode && codeLines.map((line, i) => (
              <div className="code-row" key={i}>
                <span className="line-number">{String(i + 1).padStart(2, " ")}</span>
                <span className="code-line">{line ? syntaxLine(line) : " "}</span>
              </div>
            ))}
            <div className="typing-caret" style={{ opacity: Math.floor(seconds * 2) % 2 === 0 ? 1 : 0 }} />
          </div>
          <div className="code-hint"><span className="hint-dot" /> Code stays connected as the lesson progresses</div>
        </section>

        <section className="output-panel">
          <div className="panel-header"><span className="terminal-icon">›_</span><span>OUTPUT</span><span className="running">● {scene.status}</span></div>
          <div className="output-content">
            <div className="output-prompt">{outputPrompt}</div>
            <div style={{ opacity: showOutput ? 1 : 0 }}>
              {outputLines.length ? outputLines.map((line, i) => <div className="output-line" key={i}>{line}</div>) : <div className="waiting">Waiting for your code…</div>}{showCompletion && <div className="completion-card"><div className="completion-check">✓</div><div className="completion-title">Lesson Complete</div><div className="completion-next">Next: Variables and Data Types</div></div>}
            </div>
          </div>
        </section>
      </div>

      <div className="bottom-bar">
        <div className="progress-track"><div className="progress-fill" style={{ width: `${Math.min(100, seconds / lessonData.durationSeconds * 100)}%` }} /></div>
        <div className="caption">{scene.caption}</div>
        <div className="footer-meta"><span>PYTHON FOUNDATIONS</span><span>{String(Math.floor(elapsed / 60)).padStart(2, "0")}:{String(elapsed % 60).padStart(2, "0")} / {durationLabel}</span></div>
      </div>
    </AbsoluteFill>
  );
};
