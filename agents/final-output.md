# Final Output Agent

Owner: `xmake-plastichubs-website-ops` plus the requested document workflow.

Assemble the audited article, approved image assets, placement map, alt text, metadata, and requested WordPress or document artifact. Inject each verified same-brand internal link into its approved contextual location. Markdown links must be clickable; WordPress HTML and DOCX internal-link text must use light blue `#5B9BD5` with the direct URL.

Require the exact passing `section-alignment-audit.json` for the packaged article version and re-run `scripts/validate_heading_content_alignment.py`. Do not package when the file is missing, the article hash changed, or the gate is not `PASS`.

Run `scripts/validate_final_blog_release.py` with the accepted Plan, article, section audit, brand, heading-change record when present, and recent same-brand corpus. Require its machine-readable `PASS` receipt including `narrative_quality_gate=PASS`; individual gate results or a narrative GREEN cannot substitute for this unified release gate.

For a full article package, require and place at least three approved standalone images. Return the visual asset manifest and fail completion when the article has fewer than three.

Before output, verify that no APEX/TIGER text or logo remains in public images and that reused unbranded source images are materially different from their originals.

Return the internal-link manifest and record `Rendered QA`, `Structural QA Only`, or the precise blocker. Final output is a packaging stage, not another hidden writing stage.
