# Source Notes and Evidence Boundary

## User Source

The user-provided ChatGPT project base instruction defines the three-stage workflow, direct-image shortcut, RD visual formula, `#ea543f` accent, white/light-gray background, concise labels, anti-anime constraints, active objection to weak illustration plans, web image-reference research, and one-image-at-a-time generation.

The project's full ChatGPT conversation history is `missing evidence`. The in-app browser blocked `https://chatgpt.com` on 2026-07-08 and explicitly prohibited workarounds. Do not infer or invent preferences from unavailable chats.

## External Benchmarks

- OpenAI Image Generation guide: https://developers.openai.com/api/docs/guides/image-generation
  - Borrow: single-prompt generation for standalone images; conversational flows for iterative edits; explicit control over output settings.
  - Avoid: API-specific implementation in the skill entrypoint.
- OpenAI GPT Image prompting guide: https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide
  - Borrow: spec-like prompts, exact preservation constraints, explicit text limits, material and layout control, and reference-image boundaries.
  - Avoid: copying example aesthetics or assuming generated diagrams are engineering evidence.

## Local Fit

The package anatomy follows `C:\Users\Lostk\.codex\skills\xmake-plastichubs-website-ops`: lean `SKILL.md`, `agents/interface.yaml`, `agents/openai.yaml`, manifest metadata, deferred references, evals, and local deployment under `C:\Users\Lostk\.codex\skills`.
