#!/usr/bin/env python3
"""Transcribe narration and derive scene timing from transcript content + lesson manifest.

No hand-authored phrase anchors are required. Scene boundaries are selected from
transcript sentence starts using the lesson scene's own title, caption, code, and
output vocabulary, in order. Timings always come from Whisper word timestamps.
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path
import av
from faster_whisper import WhisperModel

ROOT = Path(__file__).resolve().parents[1]
AUDIO_FILES = [ROOT / "public/audio/lesson-01/part-01.mp3", ROOT / "public/audio/lesson-01/part-02.mp3"]
STORYBOARD = ROOT / "docs/LESSON_01_REVISED_STORYBOARD.json"
TRANSCRIPT_JSON = ROOT / "out/lesson-01/transcript.json"
TRANSCRIPT_TEXT = ROOT / "out/lesson-01/transcript.txt"
ALIGNMENT = ROOT / "src/generated-alignment.json"
TOKEN_RE = re.compile(r"[a-z0-9]+")
def toks(s): return TOKEN_RE.findall(s.lower())
def duration(path):
    with av.open(str(path)) as c:
        if c.duration is not None: return c.duration / av.time_base
        st = next((x for x in c.streams if x.type == "audio"), None)
        if st is None or st.duration is None or st.time_base is None: raise RuntimeError(f"Cannot measure audio duration: {path}")
        return float(st.duration * st.time_base)
def scene_terms(scene):
    # Derive search vocabulary from the lesson's own authored teaching content.
    text = " ".join([scene.get("title",""), scene.get("caption",""), scene.get("status",""), " ".join(scene.get("code",[])), " ".join(scene.get("output",[]))])
    stop = set("the a an and or to of for in on is are it this that with your you we our what how do does can be as from by one line code python".split())
    terms = [x for x in toks(text) if x not in stop and len(x) > 2]
    # Preserve order while de-duplicating.
    return list(dict.fromkeys(terms))
def sentence_starts(words):
    starts=[0]
    for i,w in enumerate(words[:-1]):
        raw=w["text"]
        gap=words[i+1]["start"]-w["end"]
        if (re.search(r"[.!?][\"'’)]?$",raw) and gap >= 0.08) or gap >= 0.85:
            if i+1-starts[-1] >= 5: starts.append(i+1)
    if len(words)-starts[-1] < 5 and len(starts)>1: starts.pop()
    return starts
def score_candidate(words, start_i, terms, end_limit):
    # Score transcript words shortly after a candidate sentence start.
    window=words[start_i:min(end_limit,start_i+45)]
    if not window: return 0.0
    observed={t for w in window for t in toks(w["text"])}
    if not terms: return 0.0
    return len(observed.intersection(terms))/len(set(terms))
def main():
    for p in AUDIO_FILES:
        if not p.is_file(): raise RuntimeError(f"Missing narration file: {p.relative_to(ROOT)}")
    storyboard=json.loads(STORYBOARD.read_text(encoding="utf-8"))
    scenes=storyboard.get("scenes",[])
    if not scenes: raise RuntimeError("Lesson storyboard contains no scenes.")
    model=WhisperModel("tiny.en",device="cpu",compute_type="int8",cpu_threads=2,num_workers=1)
    words=[]; offsets=[]; total=0.0; durations=[]
    for path in AUDIO_FILES:
        d=duration(path); durations.append(d); offsets.append(total)
        print(f"Transcribing {path.relative_to(ROOT)} ({d:.3f}s), offset {total:.3f}s")
        segments,info=model.transcribe(str(path),language="en",beam_size=5,word_timestamps=True,vad_filter=False,condition_on_previous_text=True)
        count=0
        for seg in segments:
            count+=1
            if seg.words:
                for word in seg.words:
                    text=word.word.strip()
                    if toks(text): words.append({"text":text,"start":round(total+max(0,float(word.start)),3),"end":round(total+min(d,float(word.end)),3)})
            else:
                for t in toks(seg.text): words.append({"text":t,"start":round(total+float(seg.start),3),"end":round(total+float(seg.end),3)})
        print(f"  {count} segments; language={info.language}")
        total+=d
    words.sort(key=lambda w:w["start"])
    if not words: raise RuntimeError("Whisper returned no words.")
    TRANSCRIPT_JSON.parent.mkdir(parents=True,exist_ok=True)
    TRANSCRIPT_JSON.write_text(json.dumps({"generatedBy":"faster-whisper","model":"tiny.en","language":"en","durationSeconds":round(total,3),"audioFiles":[p.relative_to(ROOT / "public").as_posix() for p in AUDIO_FILES],"words":words},indent=2)+"\n",encoding="utf-8")
    TRANSCRIPT_TEXT.write_text("\n".join(f"[{w['start']:.3f}-{w['end']:.3f}] {w['text']}" for w in words)+"\n",encoding="utf-8")
    starts=sentence_starts(words)
    if len(starts)<len(scenes): raise RuntimeError(f"Transcript has only {len(starts)} sentence candidates for {len(scenes)} lesson scenes.")
    # Select all scene boundaries globally rather than greedily. A locally
    # strong match can otherwise leave no valid place for later scenes.
    min_scene_seconds=8.0
    candidate_rows=[]
    for ix,scene in enumerate(scenes[1:], start=1):
        terms=scene_terms(scene)
        remaining=len(scenes)-ix-1
        earliest=min_scene_seconds
        latest=total-min_scene_seconds*(remaining+1)
        row=[]
        for pos,word_i in enumerate(starts[1:], start=1):
            t=words[word_i]["start"]
            if t < earliest: continue
            if t > latest: break
            score=score_candidate(words,word_i,terms,len(words))
            row.append({"pos":pos,"time":t,"score":score})
        if not row:
            raise RuntimeError(f"No possible transcript boundaries for scene {ix+1} ({scene.get('title','untitled')}) while preserving {min_scene_seconds:.0f}s minimum scene duration.")
        candidate_rows.append(row)
    # Dynamic programming: maximize total content-match score subject to
    # ordered boundaries and minimum scene duration, including final scene.
    states=[]
    for scene_idx,row in enumerate(candidate_rows):
        next_states=[]
        for cand in row:
            if scene_idx==0:
                if cand["time"] < min_scene_seconds: continue
                next_states.append({"cand":cand,"total":cand["score"],"path":[cand]})
            else:
                best=None
                for prev in states:
                    if cand["time"]-prev["cand"]["time"] < min_scene_seconds: continue
                    item={"cand":cand,"total":prev["total"]+cand["score"],"path":prev["path"]+[cand]}
                    if best is None or item["total"]>best["total"]: best=item
                if best is not None: next_states.append(best)
        states=next_states
        if not states:
            scene_num=scene_idx+2
            raise RuntimeError(f"No ordered transcript boundary sequence can fit scene {scene_num} ({scenes[scene_num-1].get('title','untitled')}) while keeping every scene at least {min_scene_seconds:.0f}s. Review the storyboard scene order/content against the narration.")
    valid=[s for s in states if total-s["cand"]["time"]>=min_scene_seconds]
    if not valid:
        raise RuntimeError(f"No complete scene timeline can fit {len(scenes)} scenes of at least {min_scene_seconds:.0f}s into {total:.1f}s narration.")
    best=max(valid,key=lambda s:s["total"])
    chosen=[{"index":0,"score":1.0}]
    for scene_idx,cand in enumerate(best["path"],start=1):
        chosen.append({"index":cand["pos"],"score":cand["score"]})
        print(f"Scene {scene_idx+1:02d} topic match {cand['score']:.2f}: {scenes[scene_idx].get('title','')}")
    boundaries=[0.0]+[words[starts[c["index"]]]["start"] for c in chosen[1:]]+[total]
    if any(boundaries[i+1]-boundaries[i] < 8 for i in range(len(boundaries)-1)):
        raise RuntimeError("Internal alignment error: minimum scene duration constraint was not respected.")
    output=[]
    for i,scene in enumerate(scenes):
        output.append({"id":int(scene.get("id",i+1)),"title":scene.get("title",f"Scene {i+1}"),"caption":scene.get("caption",""),"status":scene.get("status",""),"code":scene.get("code",[]),"output":scene.get("output",[]),"prompt":scene.get("prompt"),"errorCode":scene.get("errorCode"),"errorOutput":scene.get("errorOutput"),"errorPrompt":scene.get("errorPrompt"),"correctedCode":scene.get("correctedCode"),"start":round(boundaries[i],3),"end":round(boundaries[i+1],3),"transcriptTopicMatch":round(chosen[i]["score"],3)})
    payload={"generated":True,"method":"whisper-transcript-topic-boundaries","model":"tiny.en","durationSeconds":round(total,3),"part2StartSeconds":round(durations[0],3),"audioTracks":[{"src":"/"+p.relative_to(ROOT).as_posix(),"start":round(offsets[i],3)} for i,p in enumerate(AUDIO_FILES)],"scenes":output}
    ALIGNMENT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(f"Wrote transcript and {len(output)} transcript-derived scenes; duration {total:.3f}s")
if __name__=="__main__":
    try: main()
    except Exception as e:
        print(f"ERROR: {e}",file=sys.stderr); sys.exit(1)
