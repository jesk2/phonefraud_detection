# FraudCallBench Sample Dataset (Prototype)

This folder contains a small hand-crafted prototype of the dataset you described for multi-turn scam call modeling.

## Files

- `sample_fraudcallbench.jsonl` — 5 example conversations, one JSON object per line.

## JSONL Schema (per conversation)

Each line is a JSON object with the following fields:

- `conversation_id` (string): Unique ID for the call.
- `label` (string): `"scam"` or `"legit"`.
- `scam_type` (string): e.g., `"tech_support"`, `"irs"`, `"bank"`, `"delivery"`, `"refund"`.
- `early_detection_target_turn` (int or null): The turn index at or before which a model should ideally flag the call as a scam. `null` for legitimate calls.
- `turns` (list): Ordered list of turn objects.

Each turn object has:

- `turn_id` (int): 1-based index within the conversation.
- `speaker` (string): e.g., `"scammer"`, `"victim"`, `"agent"`, `"customer"`.
- `text` (string): Raw utterance text.
- `persuasion_stage` (int):
  - 0 – neutral conversation
  - 1 – rapport building
  - 2 – authority claim
  - 3 – urgency / pressure
  - 4 – threat / fear
  - 5 – financial or credential request
- `manipulation_features` (object): sparse boolean-like flags capturing tactics, e.g.:
  - `authority`
  - `urgency`
  - `threat`
  - `verification`
  - `emotional_pressure`
  - `scarcity`
  - `reciprocity`
  - `payment_request`

This structure reflects your goals:

- Multi-turn conversation modeling
- Persuasion trajectory labels
- Scam type labels
- Psychological manipulation features
- Early detection targets (via `early_detection_target_turn`)

You can now load this file in a notebook and iterate on schema, additional fields, or generation scripts before scaling up to a larger dataset.