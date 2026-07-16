# Compiled Targets

- OK: `True`
- Targets: `2`
- Pass: `2`
- Warn: `0`
- Block: `0`

## Target Transforms

| Target | Status | Native Surface | Adapter Mode | Permissions | Degradation | Generated Files |
| --- | --- | --- | --- | --- | --- | --- |
| `openai` | `pass` | OpenAI-style interface metadata plus neutral Agent Skills source | `metadata-adapter` | `none` | `Uses web image search and image generation when exposed by the client; otherwise returns a verified English prompt.` | targets/openai/adapter.json, targets/openai/agents/openai.yaml |
| `generic` | `pass` | Agent Skills compatible neutral package | `agent-skills-compatible` | `none` | `Prompt-only fallback when image search or generation tools are unavailable.` | targets/generic/adapter.json |

## Native Behavior Contracts

### openai

- Native surface: OpenAI-style interface metadata plus neutral Agent Skills source
- Activation: Use frontmatter description for catalog routing and targets/openai/agents/openai.yaml for display name, default prompt, and compatibility metadata.
- Resources: Ship the neutral source tree and expose OpenAI-facing interface metadata as a generated companion file.
- Scripts: Keep scripts as local package resources; expose help-smoke and permission metadata for reviewer approval before execution.
- Permission enforcement: `metadata-only`; native enforcement `False`
- Review artifacts: targets/openai/agents/openai.yaml, targets/openai/adapter.json, reports/review-studio.html

### generic

- Native surface: Agent Skills compatible neutral package
- Activation: Use SKILL.md name and description; consumers decide automatic or manual activation.
- Resources: Preserve references, scripts, assets, evals, reports, and adapter metadata as relative package resources.
- Scripts: Expose script and permission metadata for downstream clients or installers to enforce.
- Permission enforcement: `consumer-enforced-or-metadata-only`; native enforcement `False`
- Review artifacts: targets/generic/adapter.json, reports/review-studio.html


## Failures

- None

## Warnings

- None
