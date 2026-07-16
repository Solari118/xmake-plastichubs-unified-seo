# Reference Scan

Skill: `b2b-machining-image-generator`

## Why This Step Exists

Use a short benchmark pass before authoring the package in depth. External benchmark objects should define the pattern ceiling. Local files are used afterward only to calibrate fit, privacy, naming, and compatibility.

## Current Skill Anchor

- Title: `B2B Machining Image Generator`
- Description: Diagnose B2B industrial manufacturing content, design high-value visual concepts, research relevant reference images, produce RapidDirect-style technical illustration prompts, and generate standalone images for CNC machining, surface finishing, electroplating, injection molding, tooling, materials, defects, and manufacturing processes. Use when the user asks to visualize manufacturing articles, create industrial technical illustrations, compare process or failure states, or directly generate B2B machining images. Do not use for precision engineering drawings, tolerance-certified diagrams, generic marketing art, logos, or unrelated image editing.

## Scan Focus

- **Execution pattern**: There is deterministic logic in scripts, so compare how strong references separate prose from executable steps.
- **Portability pattern**: The package carries neutral metadata, so scan how good references preserve semantics across targets without forking source.
- **Method pattern**: Use the core job description as the anchor for comparison: Diagnose B2B industrial manufacturing content, design high-value visual concepts, research relevant reference images, produce RapidDirect-style technical illustration prompts, and generate standalone images for CNC machining, surface finishing, electroplating, injection molding, tooling, materials, defects, and manufacturing processes. Use when the user asks to visualize manufacturing articles, create industrial technical illustrations, compare process or failure states, or directly generate B2B machining images. Do not use for precision engineering drawings, tolerance-certified diagrams, generic marketing art, logos, or unrelated image editing.

## Priority Rule

- External benchmark objects set the pattern ceiling. User references refine taste and standards. Local files only calibrate fit, risk, and compatibility.

## External Benchmark Objects

### https://developers.openai.com/api/docs/guides/image-generation
- Category: `general`
- Borrow: Extract the strongest reusable method, structure, or execution pattern.
- Avoid: Do not copy brand language, heavyweight process, or source-specific constraints.

### https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide
- Category: `general`
- Borrow: Extract the strongest reusable method, structure, or execution pattern.
- Avoid: Do not copy brand language, heavyweight process, or source-specific constraints.

## User-Supplied References

### User-provided ChatGPT project base instructions for B2B machining image generation; full project chat history unavailable due browser policy and must be treated as missing evidence.
- Category: `taste`
- Learn from: Learn what quality, tone, workflow shape, or operating standard the user wants to preserve.
- Do not copy: Do not copy wording, confidential material, or source-specific implementation details.

## Local Fit Check

### Match the local Codex deployment anatomy used by C:\Users\Lostk\.codex\skills\xmake-plastichubs-website-ops, including agents/interface.yaml and agents/openai.yaml.
- Category: `general`
- Keep in mind: Keep the new skill compatible with real local constraints that matter.
- Do not inherit: Do not inherit private or outdated patterns just because they already exist locally.

## Borrow Plan

- External benchmark first: let high-quality public references define the upper bound for method, structure, execution, or portability.
- User references second: use them to understand taste, standards, and directional preferences without copying source phrasing.
- Local fit third: use local assets only to detect naming conflicts, private dependencies, or compatibility constraints.
- Borrow patterns, not prose: extract loops, boundaries, metadata, and operator flow without copying source-specific language.
- Keep the package light: reject any borrowed pattern that increases context cost faster than it increases reliability.
- Apply only the benchmark patterns that fit the chosen archetype, gates, and context budget.

## Non-Goals

- Do not copy source prose or branding into the new skill.
- Do not import gates that cost more context than they save.
- Do not use benchmark scanning to justify scope creep.
- Do not let local historical habits outrank stronger public benchmarks.
