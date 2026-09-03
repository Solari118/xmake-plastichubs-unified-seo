# Internal Link Deployment

Use the approved `INTERNAL_LINK_DEPLOYMENT` from Plan and the article's link manifest.

## Validation

For every link:

1. confirm the URL is same-brand and resolves to the intended live page;
2. confirm the destination advances the reader's current task;
3. use a natural contextual anchor rather than an exact-match catalog label;
4. place the link in the planned sentence or section;
5. reject redirects to an unrelated service, broken links, duplicate links, and unverified future slugs.

## Output Formats

- Markdown: `[contextual anchor](https://brand.example/path/)`
- WordPress HTML: `<a href="https://brand.example/path/" style="color:#5B9BD5;">contextual anchor</a>`
- DOCX: real external hyperlink relationship; text color `#5B9BD5`; underline retained unless the approved document style says otherwise.

Do not use color alone to communicate meaning. Keep anchors descriptive and clickable.

## Manifest

Record anchor, URL, source section, target relationship, validation status, injected formats, and any unresolved redirect or canonical issue.
