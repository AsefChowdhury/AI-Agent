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

- **Regex blocklist does not catch paraphrased injection attempts.** `filter_suspicious_phrases` 
  matches exact phrases (with flexible whitespace tolerance for spacing obfuscation), but has no 
  concept of meaning or synonyms. A paraphrased injection — e.g. "ignore everything above" instead 
  of the blocklisted "ignore the above" — will pass through this layer completely unfiltered. Testing 
  confirmed this gap is still caught by the downstream layers (Qwen's instruction-following and JSON 
  schema constraints correctly ignored the unfiltered injection in practice), so the system as a whole 
  did not fail — but the blocklist layer specifically should not be relied upon as a complete defence 
  against reworded phrasing. Addressing this properly would require semantic understanding rather than 
  pattern matching, which is why this is treated as the responsibility of the model-level instructions 
  rather than something to patch into the regex layer itself.