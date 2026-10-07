# Refactor Backlog

- Extract shared `post_to_ollama(payload)` helper from `post_request_and_extract_data` — 
  currently conflates "make HTTP request" with "assume JSON parsing," which only fits Qwen's 
  use case. A separate one-liner was written for Llama Guard's plain-text response instead 
  of refactoring, since only 2 call sites exist so far.