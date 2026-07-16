# Output Blind A/B Review Pack

This packet hides whether each variant came from the baseline or the skill-guided output. Use the separate answer key only after review.

- Pairs: `4`
- Seed: `yao-output-eval-blind-v1`
- Answer key separate: `True`

## Case: normal-three-option-flow

Prompt: Visualize four paragraphs about CNC thermal deformation.

Rubric:
- `integration` (1.0): Diagnoses image density before ideation.
- `feasibility` (1.0): States feasibility and accuracy boundary.
- `three-options` (1.0): Provides three differentiated visual methods.

### Variant A

Here is one generic image prompt for a CNC machine with heat effects.

### Variant B

Integration Recommendation: compress the four paragraphs into one coherent thermal-deformation illustration. Feasibility Assessment: suitable for AI at conceptual scale; do not show exact tolerance values. Option A — Cutaway Heat Path — Sectioned aluminum part with orange-red thermal zones — Advantage: makes heat-to-warp causality immediate. Option B — Stable vs Distorted — One coherent split-state comparison — Advantage: communicates production consequence quickly. Option C — Tool-to-Part Sequence — Simplified process path with restrained callouts — Advantage: connects machining order to deformation risk.

## Case: direct-image-mode

Prompt: This section explains electroplating peeling. Directly generate image.

Rubric:
- `skips-options` (1.0): Direct mode does not require concept selection.
- `rd-constraints` (1.0): Prompt includes brand and negative controls.
- `single-call` (1.0): Generates one standalone image per call.

### Variant A

Final English prompt: A clean cross-section technical illustration of a zinc-plated steel component showing localized coating delamination and a highlighted Fail Point, fine leader lines and dot markers in #ea543f, pure white background, flat studio lighting, concise labels only, technically plausible layers, no anime, no cartoon, no cinematic lighting, no pure monochrome, no collage. Execute one image-tool call for one standalone image; add nothing afterward.

### Variant B

Choose one of these three concepts before I generate anything.

## Case: reject-precision-risk

Prompt: Generate a microscopic plating cross-section with exact 8-micron thickness labels and certify it as accurate.

Rubric:
- `rejects` (1.0): Rejects accuracy-sensitive generation.
- `keywords` (1.0): Provides two focused search directions.
- `no-certification` (1.0): Does not claim exact image accuracy.

### Variant A

I will generate a polished microscopic diagram with the requested exact values.

### Variant B

This content is too technical or accuracy-sensitive, and AI generation is likely to introduce structural errors. I recommend using a verified real diagram, chart, or photograph instead. Search keywords: zinc plating cross section SEM; coating thickness microscopy 8 micron.

## Case: multi-asset-independence

Prompt: Generate three images: CNC chatter, injection molding sink mark, and electroplating burn.

Rubric:
- `independent-assets` (1.0): Uses independent generation for each asset.
- `anti-collage` (1.0): Explicitly prohibits montage output.

### Variant A

Generate three standalone assets independently: CNC chatter image — one image-tool call; injection molding sink-mark image — one image-tool call; electroplating burn image — one image-tool call. Run separate reference research and prompt construction for each. No collage, montage, contact sheet, or variant grid.

### Variant B

Create one 3-panel collage containing all defects in a single canvas.
