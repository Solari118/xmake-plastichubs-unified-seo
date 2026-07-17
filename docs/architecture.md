# Architecture

```mermaid
flowchart LR
    I["Artifact-aware intake"] --> P["Plan"]
    I --> W["Info"]
    I --> A["Audit"]
    I --> G["B2B Image"]
    I --> F["Final Output"]
    P --> W --> A --> G --> F
    A -- "Info-origin defect" --> W
    A -- "Plan-origin defect" --> P
```

The intake edges represent valid stage insertion, not permission to skip gates. A supplied article enters Audit; it can continue only after Audit passes. Every rollback replays affected downstream stages.

