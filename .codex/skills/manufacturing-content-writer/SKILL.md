---
name: manufacturing-content-writer
description: Internal compatibility reference for legacy manufacturing-writing calls. Use only when manufacturing-blog-writer explicitly requests a bounded supporting rule. Delegate article drafting and revision to manufacturing-blog-writer; do not route user article requests here or create a parallel article context.
---

# Manufacturing Content Writer Compatibility Module

The current Info authority is `../manufacturing-blog-writer/SKILL.md`.

This module preserves the former skill name for compatibility. It may return a bounded process/material writing note when explicitly requested by Info, but it must not create a separate draft, alter the Plan brief, issue an Audit verdict, or load legacy project snapshots.

