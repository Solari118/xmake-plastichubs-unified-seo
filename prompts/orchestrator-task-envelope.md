# Orchestrator Task Envelope

Populate only verified fields:

- `run_id`
- `entry_point`
- `task_mode`
- `detected_artifact`
- `requested_output`
- `user_constraints`
- `approved_evidence_paths`
- `raw_conversation_forwarding: false`

Do not insert chain-of-thought, unrelated chat history, credentials, or unfiltered legacy instructions.

