# Voice Cloning

[My Research Frameworks](https://standardgalactic.github.io/voice-cloning/)

A short, first-person audio introduction to my research in philosophy, mathematics, physics, cognitive science, and computational systems.

## Overview

My research investigates how distinctions arise, persist, transform, and become admissible within systems whose histories cannot simply be reversed.

Rather than treating objects, identities, observations, and decisions as independently given, I examine the constraints and processes through which they become distinguishable and operationally meaningful.

This recording provides a concise introduction to several interconnected research programmes.

## Research Frameworks

**RSVP (Relativistic Scalar-Vector-Entropy Plenum)** investigates a constraint-first account of physical reality using scalar capacity, vector flow, and entropy. It explores the emergence of physical structure and temporal ordering through irreversible transformation.

**Spherepop Calculus and Spherepop OS** develop a computational framework organized around admissible state transitions, provenance, verification, refusal, and irreversible histories. Identity is treated as something established through a history of transformations rather than a static label.

**MEM|8** explores reconstructive memory through resonance, interference, phase relationships, and contextual constraints. It investigates retrieval as an active reconstruction process rather than straightforward access to stored representations.

**CLIO, HYDRA, and TARTAN** address structured reasoning, concurrent scheduling, and locally coordinated computation, respectively.

**Admissibility and Irreversibility** investigate the distinction between what can be described, constructed, verified, and legitimately committed as an action, particularly under uncertainty and conditions of limited reversibility.

**Distinction, Continuity, and Reconstruction** examine how identity persists through change, how representations conceal discontinuities, and why successful reproduction does not necessarily establish preservation of the original state or capability.

These frameworks are ongoing research programmes rather than completed or empirically established theories.

## Audio Production

The narration was generated using the [Hume AI Text-to-Speech Playground](https://app.hume.ai/tts/playground), using a custom voice created from a short recording of my natural speech.

The resulting synthetic narration closely resembles my own voice, although its delivery is slightly more restrained than my ordinary speaking style.

The recording was exported as an MP3 and edited locally using FFmpeg to remove an extraneous word at the end.

The final audio is approximately five minutes and forty-two seconds long.

## Technical Details

The final audio file is named `my-research-frameworks.mp3`.

The original narration was approximately 5 minutes and 44 seconds long. The final trim was performed using:

```bash
ffmpeg -i my-research-frameworks.mp3 \
  -t 00:05:41.75 \
  -c:a libmp3lame -q:a 2 \
  my-research-frameworks-trimmed.mp3
```

The project preserves a distinction between the original spoken voice sample, the synthesized narration, and the final edited recording.

## Purpose

This project is intended as a compact spoken introduction to my research rather than an exhaustive treatment of any individual framework.

It also documents a practical experiment in generating a recognizable first-person narration from a short voice sample, allowing the research to be presented in a consistent voice without requiring a complete manual recording.

### Hume AI Free Tier

At the time of this experiment (November 2026), Hume AI's Text-to-Speech Playground offered a free monthly allowance of 10,000 characters, equivalent to approximately ten minutes of generated speech, depending on the length of the text and speaking rate.

The narration of *My Research Frameworks* consumed 4,961 characters, approximately half the monthly allowance, and produced a recording of about five minutes and forty-four seconds before editing.

The experiment required no paid subscription. I supplied a short sample of my own voice, generated the narration from a prepared script, downloaded the resulting audio, and trimmed the ending locally using FFmpeg.

## Author

**Flyxion**  
Independent Researcher

[GitHub: standardgalactic](https://github.com/standardgalactic/voice-cloning/)
