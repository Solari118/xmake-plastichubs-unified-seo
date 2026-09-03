# Context Isolation Policy

## Objective

Prevent phase prompts, scratch reasoning, private research, and legacy rules from overwriting or contaminating another phase.

## Rules

1. The orchestrator sees route state; specialists see only declared handoff inputs.
2. Use one namespace per `run_id` and one subdirectory per stage.
3. Pass artifact files, not the complete conversation transcript.
4. Plan cannot edit article copy. Info cannot change strategy silently, but must receive and execute the selected structure/style reference map. Audit cannot treat its proposed wording as accepted copy. Image cannot infer unapproved technical labels. Final Output cannot rewrite claims. Performance Review can recommend a versioned rollback but cannot silently replace Plan or Info artifacts.
5. Private evidence remains tagged `Internal — Not for Publication` and is omitted from Image and Final Output unless a specific approved fact is required.
6. `data/raw/legacy-projects/` is never included in automatic retrieval, prompt assembly, or public output.
7. A rollback passes only the defect classification, affected fields/passages, acceptance criteria, and artifact versions.
8. Every stage starts with a clean scratch context. Durable state lives in versioned artifacts and the route trace.
9. Selected competitor reference records may pass from Plan to Info only as structure, pacing, evidence-form, and high-level style descriptors plus source pointers. Do not pass copied prose or authorize imitation of distinctive expression.

## Contamination Failures

- a specialist adopts another phase's role;
- legacy instructions override canonical policies;
- private competitor or source data appears in public copy or image text;
- a downstream stage reads unrelated upstream scratch files;
- a new artifact overwrites its accepted predecessor.

Any contamination failure blocks final output until repaired and re-audited.
