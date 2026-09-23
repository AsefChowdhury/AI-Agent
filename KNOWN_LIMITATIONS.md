# Known Limitations / TODO

- **No user-facing rejection message on frontend.** When a note is rejected by the guardrails 
  pipeline, the frontend just receives `{"result": null}` with no explanation shown to the user.

- **Prompt injection defences are layered but not exhaustive.** Current defences (role separation, 
  regex blocklist, delimiters, JSON schema enforcement, word-count anomaly detection, Llama Guard 
  classification) cover known attack patterns but are not a complete solution — this is an open, 
  industry-wide problem. Further mitigation (e.g. model fine-tuning for instruction hierarchy) was 
  ruled out as out of scope (no training infrastructure or dataset available).

- **`strip_formatting_symbols` cannot distinguish markdown headers from other legitimate uses of `#`.** 
  The function strips all `#` characters indiscriminately via `re.sub(r'#', '', text)`, which correctly 
  removes markdown heading markers (`# Heading`) but also incorrectly strips `#` used as part of real 
  note content (e.g. `#24 LeBron James`, hashtags, numbering). A more targeted regex 
  (e.g. `^#+\s` to only match `#` at the start of a line followed by whitespace) would fix this, but 
  was deliberately deferred: for this app's actual use case (student notes, where `#` is overwhelmingly 
  used as a markdown header), the current behaviour is an accepted simplification given scope/deadline 
  constraints.