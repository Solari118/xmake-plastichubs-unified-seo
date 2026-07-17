# Capability Preservation Policy

The unified project preserves behavior, not merely folder names.

- Current executable specialist packages live in `skills/`.
- Original source versions live under `data/raw/legacy-projects/` and are non-executable by default.
- Root scripts and tools with execution value live in `tools/`.
- Canonical orchestration, contracts, tests, and policies live in their dedicated directories.
- Generated outputs, caches, `.git`, temporary files, and user image inputs are not capabilities and are excluded from the canonical source package.
- A source file may be superseded only when its original hash remains in the inventory and the preservation matrix names the replacement.
- No legacy source is deleted by migration.

Run `python scripts/build_inventory.py` and `python scripts/validate_project.py` after migration changes.

