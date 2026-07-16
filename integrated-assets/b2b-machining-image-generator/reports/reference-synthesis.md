# Reference Synthesis

Skill: `b2b-machining-image-generator`
- Description: Diagnose B2B industrial manufacturing content, design high-value visual concepts, research relevant reference images, produce RapidDirect-style technical illustration prompts, and generate standalone images for CNC machining, surface finishing, electroplating, injection molding, tooling, materials, defects, and manufacturing processes. Use when the user asks to visualize manufacturing articles, create industrial technical illustrations, compare process or failure states, or directly generate B2B machining images. Do not use for precision engineering drawings, tolerance-certified diagrams, generic marketing art, logos, or unrelated image editing.
- Intent confidence: `100/100` (`high`)

## Live GitHub Benchmarks

- No live GitHub benchmarks are attached yet.

## Curated World-Class Pattern Tracks

### Official skill anatomy and context discipline
- Type: `official`
- Evidence mode: `curated-pattern-track`
- Why relevant: This track matches: general fit.
- Borrow: Borrow progressive disclosure: keep the entrypoint lean and move depth into references or scripts.
- Avoid: Do not let packaging or platform concerns swallow the core job boundary.

### Hypothesis-test-learn loop
- Type: `research`
- Evidence mode: `curated-pattern-track`
- Why relevant: This track matches: compare.
- Borrow: Borrow a small hypothesis-test-learn loop so the first revision is evidence-backed.
- Avoid: Do not create experimental overhead that exceeds the skill's real risk tier.

### Minimum sufficient structure
- Type: `principles`
- Evidence mode: `curated-pattern-track`
- Why relevant: This track matches: minimal.
- Borrow: Borrow the smallest structure that makes the skill reliable and explainable.
- Avoid: Do not add files or gates that raise context cost faster than they raise trust.

## Borrow Now

- Borrow progressive disclosure: keep the entrypoint lean and move depth into references or scripts.
- Borrow a small hypothesis-test-learn loop so the first revision is evidence-backed.
- Borrow the smallest structure that makes the skill reliable and explainable.
- Learn what quality, tone, workflow shape, or operating standard the user wants to preserve.

## Avoid Now

- Do not let packaging or platform concerns swallow the core job boundary.
- Do not create experimental overhead that exceeds the skill's real risk tier.
- Do not add files or gates that raise context cost faster than they raise trust.
- Do not copy wording, confidential material, or source-specific implementation details.

## Pattern Gate

- Summary: 4 accepted, 0 deferred using threshold 3/4.
- Acceptance threshold: `3/4`
- Accepted patterns:
  - **Official skill anatomy and context discipline**: 3/4 (recurrence, generativity, boundary)
  - **Hypothesis-test-learn loop**: 4/4 (recurrence, generativity, distinctiveness, boundary)
  - **Minimum sufficient structure**: 4/4 (recurrence, generativity, distinctiveness, boundary)
  - **User-provided ChatGPT project base instructions for B2B machining image generation; full project chat history unavailable due browser policy and must be treated as missing evidence.**: 4/4 (recurrence, generativity, distinctiveness, boundary)

## Default Recommendation

- Summary: Start by borrowing this pattern: Borrow progressive disclosure: keep the entrypoint lean and move depth into references or scripts. Avoid this for the first pass: Do not let packaging or platform concerns swallow the core job boundary.
- Why: There is a real design conflict to resolve: The stated preference leans lightweight or speed-first, while the benchmark mix leans toward governance, review, or heavier evaluation structure.
- User decision required: `True`

## Visibility Mode

- Mode: `explicit`
- Reasons: design_conflict
- User note: Surface the recommendation because intent is still settling or there is a real design conflict that needs a user call.
- Reviewer note: Keep the full benchmark and synthesis evidence visible for authors and reviewers.

## Conflict Check

- **lightweight_vs_governance**: The stated preference leans lightweight or speed-first, while the benchmark mix leans toward governance, review, or heavier evaluation structure.

## Quality Lift Thesis

- Use GitHub repositories for concrete package and workflow patterns.
- Use curated official or commercial tracks for entrypoint and operator ergonomics.
- Use research tracks to justify the smallest evaluation loop that still catches regressions.
- Use principle tracks to keep the package small, boundary-aware, and outcome-driven.

## Decision Prompt

Use the recommendation by default. Only surface the underlying benchmark tradeoffs when intent is uncertain or a real design conflict needs a deliberate call.
