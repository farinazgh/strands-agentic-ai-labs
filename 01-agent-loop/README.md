# Lab 01 — Agent Loop: Lessons Learned

## 1. What changed

- Switched to Claude Sonnet 4.6 after Sonnet 5 model-access denial.
- Removed `shell` and `file_editor` from the tool registry.
- Replaced agent-managed file writing with `Path.write_text()`.
- Switched `web_fetch` from agentic to Markdown mode.
- Limited fetched content to 15,000 characters per result.
- Requested at most five sources, concurrent fetching, approximately 1,000 words and source URLs.
- Retained `context_manager="auto"` and added execution metrics.

## 2. Why we changed it

- Original: ~10 minutes, 42 tool calls (14 web, 19 shell, 9 file editor).
- Optimized: ~43 seconds, four agent loop cycles, no shell or file-editor calls.
- ~14x observed speedup; not a controlled benchmark because report scope also changed.
- Windows path and shell incompatibilities caused repeated recovery attempts.
- Nested LLM calls can introduce hidden latency and cost.
- Excessive autonomy increased execution complexity and security exposure.

## 3. Production readiness lessons

- **Model access:** Check account agreements, IAM, entitlement and regional availability.
- **Autonomy:** Use LLMs for judgment; use deterministic code for predictable operations.
- **Tool design:** Prefer narrow, reliable tools; test OS compatibility and failure handling.
- **Tool provenance:** Review implementations, dependencies, permissions and input schemas. Native tools do not require MCP.
- **Least privilege:** Remove unnecessary capabilities; sandbox code execution and protect credentials.
- **Prompt injection:** Treat fetched content as untrusted data, not instructions.
- **Execution budgets:** Enforce tool-call, retry, token and time limits programmatically; prompts alone are not hard limits.
- **Observability:** Trace tool arguments, results, errors, cycle counts, latency and token usage; redact sensitive data.
- **Context management:** Bound tool output and monitor automatic context retrieval and offloading.
- **Retrieval:** Use search for discovery and fetching for known URLs; validate HTTP status and content relevance.
- **Semantic success:** A tool reporting success can still return a 404 page.
- **Evaluation:** Compare quality, groundedness, latency, cost and reliability against a baseline; verify source citations.
- **Architecture:** Start simple and increase autonomy only when justified by the task.
