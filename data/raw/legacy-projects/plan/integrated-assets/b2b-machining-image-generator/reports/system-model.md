# System Model

Skill: `b2b-machining-image-generator`

- Stability score: `100/100`
- Stability band: `system-ready`
- Doctrine: Structure drives behavior: improve the boundary, feedback loops, drift watch, and leverage points before adding weight.

## System Boundary Map

- Owned job: Turn technical B2B manufacturing content into accurate, minimalist, brand-controlled industrial image concepts and standalone generated images.
- Output boundary: Normal mode: diagnosis and three differentiated visual options; selected or direct mode: final English prompt plus one independently generated image per request.
- Maturity assumption: `production`
- Input boundary:
  - English or Chinese manufacturing article text, a selected concept number, or text plus the direct image generation instruction.
- Non-goals:
  - Precision engineering drawings, tolerance-critical annotations, microscopic metallography, exact process data charts, generic decorative art, collage output, and unverified structural claims.
- Constraints:
  - Search relevant image references before generation when web image search is available; use #ea543f accents; white or light gray background; no anime, cartoon, cinematic lighting, pure monochrome, long in-image text, or collage.
- Standards:
  - Bilingual interaction Chinese first and English second; engineering-rational tone; concise labels; visual truthfulness; one image generated independently per tool call.
- Human judgment boundary:
  - Ask one focused clarification when the real job, output, or exclusion boundary is unclear.
  - Escalate visible tradeoffs when benchmark patterns conflict with local privacy, naming, or governance constraints.
  - Do not silently broaden the skill into adjacent jobs just because the examples are nearby.

## Feedback Loops

### Intent boundary loop

- Signal: Intent confidence score is 100/100.
- Response: Ask only the highest-leverage clarification before adding package weight.
- Evidence: reports/intent-confidence.md and reports/intent-dialogue.md

### Reference synthesis loop

- Signal: Benchmark patterns are useful only after they are abstracted into borrow and avoid guidance.
- Response: Borrow one pattern at a time and keep the rest as reviewer-visible evidence.
- Evidence: reports/reference-synthesis.md
- Current patterns:
  - Borrow progressive disclosure: keep the entrypoint lean and move depth into references or scripts.
  - Borrow a small hypothesis-test-learn loop so the first revision is evidence-backed.
  - Borrow the smallest structure that makes the skill reliable and explainable.
  - Learn what quality, tone, workflow shape, or operating standard the user wants to preserve.
  - Do not let packaging or platform concerns swallow the core job boundary.

### Output quality loop

- Signal: Generated output may fail in recurring domain-specific ways.
- Response: Apply predicted output-risk families as self-repair checks before final output.
- Evidence: reports/output-risk-profile.md
- Current risk families:
  - Screenshot and visual capture
  - Tone and specificity
  - Markdown readability
  - Citation and footnote clutter
  - Code and command safety

### Reviewer feedback loop

- Signal: Human review catches drift that static checks miss.
- Response: Capture lightweight feedback and turn repeated findings into gates or references.
- Evidence: reports/review-viewer.html and feedback records

### Lifecycle loop

- Signal: As reuse grows, the skill needs stronger gates, ownership, and regression evidence.
- Response: Promote only when the next gate improves reliability more than context cost.
- Evidence: manifest.json, reports/iteration-directions.md, and governance checks

## Delay And Drift Watch

### Trigger drift

- Watch signal: Users start invoking the skill for adjacent one-off or explanation-only requests.
- Countermeasure: Add near-neighbor exclusions and route evals before expanding workflow steps.
- Cadence: per trigger or description change

### Output drift

- Watch signal: Outputs remain valid but become generic, cluttered, or weakly aligned with the user's domain.
- Countermeasure: Refresh output-risk and artifact-design profiles, then add one self-repair check.
- Cadence: after the first 3-5 real uses
- Risk families:
  - Screenshot and visual capture
  - Tone and specificity
  - Markdown readability
  - Citation and footnote clutter
  - Code and command safety

### Reference drift

- Watch signal: Borrowed benchmark patterns no longer fit the local job or add ceremony without payoff.
- Countermeasure: Re-run reference synthesis and keep only patterns that improve the current boundary.
- Cadence: per material benchmark or product assumption change

### Governance drift

- Watch signal: Skill usage becomes team-critical while ownership, review cadence, or rollback evidence stays informal.
- Countermeasure: Promote maturity tier and add reviewer-visible lifecycle evidence.
- Cadence: monthly

## Failure Pattern Map

### Boundary failure

- Symptom: The skill handles nearby requests that were never part of the recurring job.
- Repair: Narrow the description and add explicit non-goals before adding more execution steps.

### Feedback gap

- Symptom: The skill has rules but no signal telling authors which rule should change after use.
- Repair: Turn repeated reviewer feedback into one eval, one reference note, or one self-repair check.

### Output degradation

- Symptom: The result is structurally correct but generic, cluttered, or weakly matched to the user's domain.
- Repair: Use output-risk families as pre-final checks.
- Current Risk Families:
  - Screenshot and visual capture
  - Tone and specificity
  - Markdown readability
  - Citation and footnote clutter
  - Code and command safety

### Prompt-behavior mismatch

- Symptom: The role, task, and format are copied from a prompt instead of becoming stable skill behavior.
- Repair: Convert reusable role/task/format assumptions into workflow, reports, or references.

## Highest Leverage Moves

### 2. Tune the frontmatter description

- Why: The description is the highest-leverage routing surface.
- Move: Name the recurring job, expected input, output, and strongest non-goal in compact language.

### 3. Install output self-repair checks

- Why: The likely failure families are: Screenshot and visual capture, Tone and specificity, Markdown readability.
- Move: Add only the checks that prevent recurring output mistakes.

### 4. Borrow one pattern, not a whole product

- Why: External references improve quality when reduced to structure, not copied as surface style.
- Move: Start from: Borrow progressive disclosure: keep the entrypoint lean and move depth into references or scripts.

### 5. Close the lifecycle loop

- Why: Team-reused skills need visible ownership, review cadence, and regression evidence.
- Move: Keep manifest, review viewer, and iteration directions aligned after each material change.

## Reviewer Use

- Reviewer should ask whether the skill's structure will keep producing the desired behavior after repeated real use.
- Prefer changing the system boundary, feedback loop, or leverage point before adding more prose.
- If a problem repeats, convert it into a named failure pattern and one regression check.
