# B2B Machining Image Generator

Local Codex skill and agent metadata for turning manufacturing content into professional industrial visual concepts, English image prompts, and independently generated images.

## Use

```text
Use $b2b-machining-image-generator to visualize this CNC machining article.
[paste article]
```

Direct mode:

```text
Use $b2b-machining-image-generator. 直接生成图片：
[paste content]
```

## Behavior

- Normal mode: diagnosis, feasibility decision, and exactly three differentiated visual options.
- Direct mode: silent visual judgment, bounded reference-image research, final English prompt, and one image-tool call.
- Multiple images: generated independently one by one; no collage or contact sheet.
- Accuracy boundary: no precision drawing, tolerance certification, exact microscopy, or unsupported measured values.
- Fallback: prompt-only output when image search or image generation is unavailable.

## Evidence Status

- User-provided base instruction: available.
- Official OpenAI image-generation documentation: reviewed.
- Local deployment pattern: reviewed from `xmake-plastichubs-website-ops`.
- Full ChatGPT project chat history: `missing evidence` because the in-app browser blocked `https://chatgpt.com` and prohibited workarounds.

## Local Deployment

Source package:

`C:\Users\Lostk\Documents\B2B机加工生图\b2b-machining-image-generator`

Active Codex install target:

`C:\Users\Lostk\.codex\skills\b2b-machining-image-generator`

Validate the source package before syncing the active install.
