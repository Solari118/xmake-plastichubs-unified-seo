# Architecture

```mermaid
flowchart LR
    I["Artifact-aware intake"] --> P["Plan"]
    I --> W["Info"]
    I --> A["Audit"]
    I --> G["B2B Image"]
    I --> F["Final Output"]
    I --> R["Performance Review"]
    P --> W --> A --> G --> F
    F -. "published + metrics" .-> R
    R -- "planning defect" --> P
    R -- "content defect" --> W
    R -- "link or packaging defect" --> F
    A -- "Info-origin defect" --> W
    A -- "Plan-origin defect" --> P
```

The intake edges represent valid stage insertion, not permission to skip gates. A supplied article enters Audit; it can continue only after Audit passes. Every rollback replays affected downstream stages. A published article with dated performance evidence enters Performance Review directly.
