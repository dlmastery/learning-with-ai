---
title: "Live multimodal mentorship at the full-duplex July 2026 frontier"
wave: A
section: A4
date_researched: 2026-07-25
cutoff: "2026-07-25T23:59:59-07:00"
status: complete
sources_count: 22
supersedes: "research/raw/A4-live-multimodal.md"
---

# A4 — Live Multimodal Mentorship

## Executive finding

The voice interface crossed a qualitative threshold in July 2026.

OpenAI’s GPT-Live is full duplex: it continuously listens while generating
speech and decides many times per second whether to speak, acknowledge, remain
silent, interrupt, or invoke a tool. It can delegate a difficult question to a
frontier model while maintaining the conversation. Gemini Live accepts
streaming audio, images, and video frames through an API, supports barge-in,
search and function tools, session resumption, configurable activity detection,
and 97 documented languages. Gemini 3.5 Live Translate supports more than 70
spoken languages and 2,000-plus language pairs. `VENDOR`

These are capability claims, not learning outcomes. The significance is
architectural:

> A universal mentor can now feel continuously present: listen while speaking,
> notice interruption, share silence, see selected work, point to a generated
> object, call specialists, translate naturally, and preserve one coherent
> relationship across modalities.

The mentor is not one realtime model. It is a loop connecting:

- continuous audio policy;
- scoped camera, document, and screen perception;
- a shared reactive artifact;
- grounding and execution tools;
- learner-owned state;
- teacher/family escalation;
- local speech and curriculum fallback.

This report supersedes the earlier A4 draft, which over-centered avatar
rendering and API constraints. The frontier design uses a face only when it
serves a learner; shared work, voice, pointing, and responsive representations
are the core.

---

## 1. GPT-Live changes turn-taking

OpenAI launched GPT-Live in ChatGPT Voice on 8 July 2026.

The vendor describes:

- a full-duplex architecture that listens and speaks simultaneously;
- continuous processing rather than separate messages;
- interaction decisions many times per second;
- backchannels such as short acknowledgements;
- quick overlap and interruption;
- silence when the person needs time;
- live translation;
- background delegation to a frontier model or web search while conversation
  continues;
- realtime safeguards that act during speech.

GPT-Live-1 is available to paid ChatGPT users and GPT-Live-1 mini to free users.
At the 25 July cutoff, the API is announced as coming “soon.” GPT-Live-1 itself
does not support video or screen sharing at launch; eligible subscribers use
the earlier Advanced Voice path for those modalities. `VENDOR`

Sources:

- [Introducing GPT-Live](https://openai.com/index/introducing-gpt-live/)
- [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- [GPT-Live system card](https://deploymentsafety.openai.com/gpt-live/gpt-live.pdf)

### Learning consequence

The policy can distinguish:

- a pause that means “I am thinking”;
- a pause that means “please help”;
- a learner correcting the mentor mid-sentence;
- a quiet acknowledgment that preserves flow;
- an urgent misconception requiring interruption;
- a tool call that should return only when the learner is ready.

The key metric is not merely response latency. It is **interaction appropriateness
over time**.

---

## 2. Gemini Live provides the current developer surface

The Gemini Live API uses a stateful WebSocket and accepts realtime text, audio,
and video. It can return audio, text/transcription, and function-call events.
Start-of-activity can interrupt model output. Automatic voice activity
detection is configurable, and manual activity boundaries support push-to-talk
in noisy rooms. `VENDOR`

The documented July comparison includes:

- Gemini 3.1 Flash Live with `thinkingLevel`, sequential function calling, and
  turn coverage including all video frames;
- Gemini 2.5 Flash Native Audio with asynchronous non-blocking functions,
  proactive decisions not to respond, and affect-aware dialogue;
- Google Search and custom function tools;
- session resumption and context compression;
- 128K context for native-audio output models;
- 97 documented languages.

Current documented limits include 15-minute audio-only and two-minute
audio-plus-video sessions, with session-management techniques for extension.
Native audio response mode uses transcription for text. `VENDOR`

Sources:

- [Gemini Live capabilities](https://ai.google.dev/gemini-api/docs/live-api/capabilities)
- [Gemini Live WebSocket API](https://ai.google.dev/api/live)
- [Gemini Live WebSocket guide](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket)
- [Gemini Live tools](https://ai.google.dev/gemini-api/docs/live-tools)

### Learning consequence

The product wrapper owns continuity. It must reconnect, resume, preserve the
learner’s heard transcript, maintain state, and fall back locally without making
the session feel like a fresh chatbot.

---

## 3. Translation is becoming a live relationship

Gemini 3.5 Live Translate:

- automatically detects more than 70 languages;
- supports more than 2,000 pairs rather than only English pivots;
- preserves reported intonation, pacing, and pitch;
- supports multiple languages in one interaction;
- is rolling through Translate, Meet preview, AI Studio, and the Live API.
  `VENDOR`

Source:

- [Gemini 3.5 Live Translate](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-live-3-5-translate/)

This can connect learner, teacher, family, and remote specialist across
languages. The architecture should keep:

- original speech;
- translated transcript;
- subject terminology mapping;
- uncertainty or alternate translation;
- learner-preferred explanation language;
- stable notation language;
- the right to ask for repetition or a literal rendering.

Translation fluency is not language parity. Each language still needs tutoring
and learning-outcome evaluation.

---

## 4. Seeing is a scoped action, not permanent surveillance

The mentor can receive:

- a learner-selected camera frame;
- a crop around notebook work;
- a shared screen region;
- a document page;
- an artifact node and cursor position;
- a short video sequence where motion matters.

The interface should make perception visible:

- “camera off”;
- “looking at this crop”;
- “screen shared until this step ends”;
- “frame sent to the science specialist”;
- “image retained only in the local session.”

The learner points or grants access. The mentor asks before expanding scope.
Routine handwriting or object recognition can run locally. Only ambiguous or
specialist cases leave the device.

The July Gemini API processes video as sampled frames rather than a human-like
continuous visual stream. The product should select useful changes—new work,
pointing, a diagram transition—rather than sending uninformative frames.
`VENDOR`; `INFERENCE`

---

## 5. The shared artifact is the visual center

The most useful “face” of the mentor is often:

- a diagram both parties can point at;
- the learner’s reactive notebook;
- a number line or manipulative;
- a code trace;
- a simulation;
- a proof or concept map;
- an annotated camera crop.

The mentor can say “this term,” highlight it, and wait while the learner changes
the model. Voice and object reference remain synchronized through stable node
IDs.

An avatar may add presence for language rehearsal, social stories, or learners
who benefit from facial cues. It is an optional representation, not the default
proof of liveness.

---

## 6. The continuous interaction policy

At each moment, the mentor selects among:

```text
listen
acknowledge
ask
explain
show
point
wait
call a tool
call a specialist
invite a teacher or peer
```

Inputs include:

- learner speech and interruption;
- visible work changes;
- current goal and teaching mode;
- prediction or explanation state;
- confidence and recent errors;
- language and access preference;
- tool status;
- emotional self-report or explicit request;
- privacy and consent scope.

Silence is a first-class output. A mentor that answers every sound is not
attentive.

---

## 7. Tools stay asynchronous

A live mentor may need:

- search grounding;
- curriculum retrieval;
- calculation or code execution;
- OCR;
- a proof or unit checker;
- a visual generator;
- a specialist model;
- a teacher notification.

The audio model should not invent a placeholder while a tool runs. It can:

- tell the learner what is being checked;
- invite a prediction;
- continue a related explanation;
- return the result when it fits the conversation;
- expose the grounding or verification record on the artifact.

Gemini 2.5 Live’s non-blocking function mode and GPT-Live’s reported background
delegation are current examples. `VENDOR`

---

## 8. Local continuity

Cloud speech should be a quality tier, not a requirement for learning.

Current open or local components include:

- [Sarvam Edge](https://www.sarvam.ai/products/edge): a vendor-reported sub-1GB
  speech, translation, and synthesis stack for 22 scheduled Indian languages;
- [Meta Omnilingual ASR](https://ai.meta.com/blog/omnilingual-asr-advancing-automatic-speech-recognition/):
  open recognition for more than 1,600 languages, including 500 low-resource
  languages not previously covered by AI, per Meta;
- [Voxtral](https://mistral.ai/news/voxtral/): an open 3B edge speech
  understanding model;
- [Voxtral TTS](https://mistral.ai/news/voxtral-tts/): a multilingual 4B speech
  model with an open-weight reference-voice variant.

All are `VENDOR` or vendor-run benchmark claims.

The learner device or school node can provide:

- wake and push-to-talk;
- speech recognition and synthesis;
- curriculum search;
- routine explanation and practice;
- state capture;
- queued cloud or human escalation.

When connectivity returns, the mentor resumes the relationship rather than
replaying the lesson.

---

## 9. Access modes

Full duplex must not become voice-only.

Equivalent paths include:

- text captions and editable transcript;
- switch and keyboard control;
- sign-language or human-interpreter handoff;
- slower or chunked speech;
- push-to-talk;
- noise-tolerant classroom mode;
- visual status of listening, thinking, speaking, checking, and reconnecting;
- no-camera and no-audio operation;
- replay with variable speed;
- symbol, notation, and pronunciation correction.

[WCAG 2.2](https://www.w3.org/TR/WCAG22/) remains the baseline. The H1
accessibility-first chapter will make the modes part of the core architecture,
not later accommodations.

---

## 10. Evaluation

### Component measures

- time to first useful audio;
- interruption detection and cancellation;
- false turn ends;
- silence appropriateness;
- word and concept accuracy by language and dialect;
- visual reference accuracy;
- tool-call correctness;
- reconnect and resume continuity;
- energy, data, and cost per learner hour.

### Interaction measures

- learner and mentor speak-over rate;
- proportion of useful backchannels;
- time learner spends explaining;
- successful repair after misunderstanding;
- number of references resolved on a shared artifact;
- teacher escalation quality;
- learner control of capture and transcript.

### Learning measures

- delayed unaided recall;
- transfer;
- spoken explanation quality;
- independence after scaffold fading;
- distributional gains by language, disability, device, and baseline;
- cost per successful learning hour.

Voice naturalness is not the endpoint.

---

## 11. Acceptance tests

A live multimodal mentor passes when:

1. learners can interrupt and correct it mid-speech;
2. it can listen and decide to remain silent;
3. spoken references resolve to stable artifact nodes;
4. camera and screen scope is learner-visible and time-bounded;
5. tool status and verified results remain visible;
6. reconnect preserves the coherent session;
7. original and translated speech remain traceable;
8. subject terminology is stable across languages;
9. local speech and practice continue offline;
10. text, keyboard, touch, and no-camera paths preserve the goal;
11. teachers can enter with the relevant context;
12. every retained audio, image, or transcript has a permission and expiry;
13. latency is measured end-to-end on target devices and networks;
14. language parity uses learning outcomes;
15. live use improves independent capability, not only satisfaction.

---

## Conclusion

Full duplex turns the mentor from a sequence of recorded voice messages into a
continuous collaborator.

The universal design is not a talking head. It is:

- natural listening and interruption;
- scoped perception of learner work;
- a shared object both can change;
- asynchronous tools and specialist routing;
- multilingual translation;
- learner-owned continuity;
- local operation when the cloud disappears;
- trusted people entering at the right moment.

For a learner, it should feel simple: show your work, speak in your language,
interrupt when the mentor is wrong, and keep going.

---

## Source index

1. [Introducing GPT-Live](https://openai.com/index/introducing-gpt-live/)
2. [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
3. [GPT-Live system card](https://deploymentsafety.openai.com/gpt-live/gpt-live.pdf)
4. [Gemini Live capabilities](https://ai.google.dev/gemini-api/docs/live-api/capabilities)
5. [Gemini Live API reference](https://ai.google.dev/api/live)
6. [Gemini Live WebSocket guide](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket)
7. [Gemini Live tools](https://ai.google.dev/gemini-api/docs/live-tools)
8. [Gemini 3.5 Live Translate](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-live-3-5-translate/)
9. [Gemini audio model updates](https://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/)
10. [Sarvam Edge](https://www.sarvam.ai/products/edge)
11. [Sarvam speech-to-text](https://www.sarvam.ai/speech-to-text)
12. [Meta Omnilingual ASR](https://ai.meta.com/blog/omnilingual-asr-advancing-automatic-speech-recognition/)
13. [Mistral Voxtral](https://mistral.ai/news/voxtral/)
14. [Mistral Voxtral TTS](https://mistral.ai/news/voxtral-tts/)
15. [WebRTC specification](https://www.w3.org/TR/webrtc/)
16. [Media Capture and Streams](https://www.w3.org/TR/mediacapture-streams/)
17. [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
18. [DeepTutor](https://arxiv.org/abs/2604.26962)
19. [Sierra Leone RCT](https://deepmind.google/blog/measuring-the-impact-of-learning-with-ai-in-sierra-leone-and-beyond/)
20. [SCALA proactive tutor](https://aclanthology.org/2026.acl-industry.107/)
21. [OECD Digital Education Outlook 2026](https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/01/oecd-digital-education-outlook-2026_940e0dd8/062a7394-en.pdf)
22. [C2PA specifications](https://spec.c2pa.org/specifications/)
