# Memory Boundary

This directory defines memory interfaces; it does not store raw conversations.

- Per-run route state belongs under ignored `data/processed/runs/<run_id>/`.
- Durable project policy belongs in version-controlled `AGENTS.md`, `policies/`, `workflows/`, or skill references.
- Do not promote private source content, scratch reasoning, or user secrets into project memory.
- Cross-run learning requires explicit user approval and a reviewed change.

