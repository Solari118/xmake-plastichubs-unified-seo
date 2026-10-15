# 安全与信任检查 / Security and trust review

日期 / Date: 2026-10-15

- 来源 / Source: a company-neutral instruction adaptation of the active local manufacturing Blog workflow.
- 文件边界 / File boundary: an explicit allowlist in `scripts/verify_package.py`; the build rejects extra files, symlinks, binary files, run data folders, and common private-source markers.
- 权限 / Permissions: this Skill has no credential, network client, install hook, or command that uploads local run files. A user must separately authorize live CMS changes.
- 已运行 / Executed: ZIP reopen and per-file SHA-256 verification; isolated extraction and verification; repository structure validation and tests.
- 限制 / Limit: static text screening cannot establish that every future user input is safe. Review the staged Git diff before each public push.

The package contains no populated company records. Existing repository history is outside this package review.
