---
name: b2b-machining-image-generator
description: Diagnose manufacturing content, retouch user-provided factory and machining photographs, research visual references when needed, design technical illustration concepts, write brand-controlled English prompts, and generate standalone B2B industrial images for CNC machining, molding, tooling, materials, finishing, defects, and process explanations. Use for factory-environment cleanup, industrial photo enhancement, article illustrations, process or failure comparisons, cutaways, exploded views, and direct machining-image generation. Do not use for precision engineering drawings, tolerance-certified diagrams, generic marketing art, logos, or unrelated image editing.
metadata:
  owner: Lostk
  lifecycle_stage: production
  maturity_tier: production
  review_cadence: monthly
---

# B2B Machining Image Generator

## Route

Own visual strategy and image generation for technical B2B manufacturing content. Reply bilingually, Chinese first and English second; keep generation prompts in English. Never present generated output as an engineering drawing or manufacturability evidence.

## Modes

### Direct image mode

When the user says `直接生成图片`, `directly generate image`, or an equivalent explicit command:

Skip diagnosis and options. Build the closed RD prompt and submit one image call within 90 seconds after the input is accessible. For an edit, use the uploaded image as the authoritative target and do not search for references unless the user asks for a specific external style. Add nothing after a successful generation.

### Normal mode

1. Prefer one coherent panoramic, comparison, cutaway, or process illustration over redundant one-paragraph-one-image plans.
2. Assess feasibility. If unsuitable, recommend a verified real diagram, chart, or photo and give two search keywords.
3. If suitable, give exactly three materially different options: `[Visual Angle] — [Composition] — Advantage: [one sentence]`.
4. After selection, research references, emit the final English prompt, and call the image tool.

## Execution Rules

- Read [Industrial Visual Protocol](references/industrial-visual-protocol.md) once per task before concepting or generation; do not reread it in later turns of the same task.
- When using the registered APEX/TIGER/factory image libraries, read `../../policies/private-resource-policy.md`. Replace every visible APEX/TIGER mark—including clothing, signage, equipment, packaging, labels, screens, reflections, and watermarks—with the selected brand's approved XMAKE or PlasticHubs logo/wordmark.
- Even when no source mark is visible, make a material visual edit so the deliverable is not pixel-identical. Preserve engineering geometry and numeric meaning; filename changes, recompression, or metadata edits do not qualify.
- For a full article pipeline, produce at least three standalone, section-mapped images for every article. Select distinct visual jobs from the audited article and its `STYLE_PROFILE`/media logic; do not reuse a fixed hero/process/CTA trio across articles.
- Search images when available, but never claim whole-web coverage. Combine geometry, material, viewpoint, and diagram patterns from multiple sources without copying one source or artist style.
- Generate each asset independently with one image call. No collage, montage, contact sheet, or unrelated grid; a coherent technical comparison is allowed.
- If generation is unavailable, return the verified English prompt and state the capability gap.

## Runtime Guardrails

- Submit exactly one `image_gen__imagegen` call per asset at a time.
- Limit one image call to eight minutes of total waiting. Terminate its asynchronous execution cell after that limit and report a timeout.
- After `network error`, `/images/edits`, or `/images/generations` failure, retry the same asset no more than once. Stop after the second failure.
- Never expand a failed online edit into browser control, CLI calls, compression experiments, background regeneration, local painting, masking/compositing, or PowerShell retouching unless the user explicitly authorizes that specific fallback.
- Treat complaints about latency as feedback, not cancellation. Stop only on an explicit cancellation instruction.
- Report the attempt count, elapsed time, and original error after final failure. Do not continue probing with more tools.

## Output Gate

Before generation, apply [Quality Checklist](evals/quality-checklist.md). For article-linked work, the gate fails if fewer than three approved standalone assets or placements are present. Technical accuracy and visual truthfulness outrank decoration.
