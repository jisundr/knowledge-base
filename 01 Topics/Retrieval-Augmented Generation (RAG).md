---
type: topic
tags: [ai-engineering, rag]
---

# Retrieval-Augmented Generation (RAG)

Prevents model hallucinations by feeding relevant, grounded source data (e.g., internal company policies or legal documents) into the LLM's context window alongside the user's question.

## Pipeline

1. **Ingestion and Chunking**: Source documents enter the pipeline and are broken into fixed-size chunks.
2. **Embedding and Storage**: Chunks are converted to vector embeddings and stored in a vector database. See [[Embeddings and Vector Search]].
3. **Retrieval**: On a user question, retrieve the chunks most similar to the query.
4. **Augmented Prompting**: Inject the retrieved context and the user query into the model's context window.
5. **Grounded Generation**: The model answers rooted in the retrieved factual context.

## Production use cases

- Enterprise knowledge RAG: internal search for HR desks, legal teams, customer service chatbots.

## Related

- [[AI Agents and Tool Use]]
- [[AI Engineer Skill Stack]] (Tier 2)

## Sources

- [[Essential Skills for Becoming an AI Engineer - RAG, AI Agents & More]]
