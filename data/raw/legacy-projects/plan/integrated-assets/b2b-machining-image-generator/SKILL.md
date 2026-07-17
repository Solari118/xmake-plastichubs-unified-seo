---
name: b2b-machining-image-generator
description: Diagnose manufacturing content, research visual references, design technical illustration concepts, write brand-controlled English prompts, and generate standalone B2B industrial images for CNC machining, molding, tooling, materials, finishing, defects, and process explanations. Use for article illustrations, process or failure comparisons, cutaways, exploded views, and requests to directly generate machining images. Do not use for precision engineering drawings, tolerance-certified diagrams, generic marketing art, logos, or unrelated image editing.
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

Skip diagnosis and options. Silently choose the strongest visual angle, run the reference scan, build the closed RD prompt, emit it immediately before the image call, and generate one standalone image. Add nothing afterward.

### Normal mode

1. Prefer one coherent panoramic, comparison, cutaway, or process illustration over redundant one-paragraph-one-image plans.
2. Assess feasibility. If unsuitable, recommend a verified real diagram, chart, or photo and give two search keywords.
3. If suitable, give exactly three materially different options: `[Visual Angle] — [Composition] — Advantage: [one sentence]`.
4. After selection, research references, emit the final English prompt, and call the image tool.

## Execution Rules

- Read [Industrial Visual Protocol](references/industrial-visual-protocol.md) before concepting or generation.
- Search images when available, but never claim whole-web coverage. Combine geometry, material, viewpoint, and diagram patterns from multiple sources without copying one source or artist style.
- Generate each asset independently with one image call. No collage, montage, contact sheet, or unrelated grid; a coherent technical comparison is allowed.
- If generation is unavailable, return the verified English prompt and state the capability gap.

## Output Gate

Before generation, apply [Quality Checklist](evals/quality-checklist.md). Technical accuracy and visual truthfulness outrank decoration.
