# Output Risk Profile

Skill: `b2b-machining-image-generator`

## Why This Exists

Generated skills often fail in small output details: generic headings, cluttered citations, fragile screenshots, weak Markdown rendering, or missing execution assumptions. This profile predicts the most likely output mistakes before the skill is used heavily.

## Matched Risk Families

### Screenshot and visual capture
- Matched keywords: screenshot, image, visual, screen
- Score: `4`

### Tone and specificity
- Matched keywords: marketing, copy, article, content
- Score: `4`

### Markdown readability
- Matched keywords: md, table, report
- Score: `3`

### Citation and footnote clutter
- Matched keywords: citation, research, reference
- Score: `3`

### Code and command safety
- Matched keywords: script, api
- Score: `2`

## Likely Output Mistakes

- Screenshots can be captured from the wrong state, wrong viewport, or wrong crop.
- Missing screenshots can cause the skill to invent visual references instead of declaring the gap.
- Headings and summaries can drift into generic, interchangeable language.
- The output can sound polished but lose the user's actual taste, audience, or scenario.
- Tables can render as dense grids with weak hierarchy or poor mobile readability.
- Long bullets can make the output look complete while hiding the actual decision logic.

## Output Constraints To Apply

- Never invent a screenshot; state when visual evidence is missing.
- Record the source, viewport, and crop intent for any screenshot-dependent output.
- Anchor titles and summaries in the user's audience, object, and concrete outcome.
- Avoid placeholder phrases such as comprehensive guide, ultimate solution, or key insights unless the source demands them.
- Use tables only when comparison is the main job; otherwise prefer compact cards or grouped bullets.
- Keep table cells short and move explanations below the table.

## Self-Repair Checks

- Check that every screenshot reference points to a real provided or generated asset.
- Reword any visual instruction that depends on an unseen screen state.
- Replace generic title candidates with scenario-specific alternatives.
- Delete any polished sentence that could fit almost any project unchanged.
- Preview whether each table still reads well when columns are narrow.
- Convert any table with paragraph-length cells into bullets or cards.

## Reviewer Note

Use this report before deepening the package and again before approving example outputs.
