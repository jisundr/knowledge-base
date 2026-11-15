---
type: article-note
status: inbox
created: 2026-11-15
tags: [ai-engineering, test]
source: https://example.com/test-note
---

# TEST - Prompt Caching and RAG Basics

Test note for the `/ingest` command. Safe to delete.

## Prompt caching

Prompt caching stores the processed prefix of a prompt so repeated requests reuse it instead of recomputing it. Stable content (system prompt, tool definitions, large documents) goes first; variable content goes last. It cuts latency and cost for long, repeated contexts.

## RAG recap

Retrieval-Augmented Generation fetches relevant chunks from a vector store using embeddings and adds them to the prompt. Chunk size and overlap strongly affect retrieval quality. Combining prompt caching with RAG works best when the retrieved chunks are placed after the cached prefix.

## Takeaways

- New concept: prompt caching (no existing topic note).
- Existing concepts: RAG and embeddings (should extend, not duplicate).
