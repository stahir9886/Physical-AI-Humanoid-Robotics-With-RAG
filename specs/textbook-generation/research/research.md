# Research: AI-Native Physical AI & Humanoid Robotics Textbook

**Feature**: textbook-generation
**Date**: 2025-12-10
**Spec**: [Link to spec.md]

## Overview

This research document provides technical investigation and decision-making for the AI-native textbook with RAG chatbot feature. The solution encompasses a Docusaurus-based textbook frontend with a retrieval-augmented generation backend for AI-powered Q&A functionality.

## Key Findings

### Technology Research

**Docusaurus Framework**
- Decision: Use Docusaurus as the static site generator for the textbook
- Rationale: Docusaurus is purpose-built for documentation sites, supports markdown content, has built-in search capabilities, and can be easily hosted on GitHub Pages. It also allows for custom React components to embed the RAG chatbot functionality.
- Alternatives considered:
  - GitBook: More commercial, some limitations on free tier
  - VuePress: Alternative but Docusaurus has better React ecosystem integration
  - Custom solution: More development time, maintenance overhead

**Backend Technology for RAG**
- Decision: Use FastAPI for the backend RAG service
- Rationale: FastAPI provides high performance, async support, automatic API documentation, and great integration with Python ML/AI libraries like LangChain, which is essential for RAG functionality.
- Alternatives considered:
  - Flask: Less performant, less modern
  - Node.js: Possible but Python ecosystem is stronger for AI/ML tasks
  - Serverless functions: Could work but may have cold start issues

**Vector Database for Embeddings**
- Decision: Use Qdrant as the vector database for storing text embeddings
- Rationale: Qdrant offers excellent performance, scalability, good Python integration via LangChain, and has a free tier suitable for the project's needs.
- Alternatives considered:
  - Pinecone: More commercial, may exceed free tier costs
  - ChromaDB: Good alternative but Qdrant has better scalability
  - Weaviate: Also good but Qdrant integrates better with LangChain

**Database for Metadata**
- Decision: Use Neon Postgres for storing metadata and configuration
- Rationale: Neon is Postgres-compatible, offers a generous free tier, serverless scaling, and excellent performance characteristics.
- Alternatives considered:
  - Supabase: Good alternative but Neon was chosen for its serverless benefits
  - SQLite: Too limited for concurrent users
  - MongoDB: NoSQL option but Postgres is better for structured metadata

**AI/LLM Integration**
- Decision: Use OpenAI API initially with option to switch to open-source alternatives like Ollama or Hugging Face models
- Rationale: OpenAI provides high-quality, reliable responses but can be expensive. Plan to implement fallback to open-source models if needed for cost management.
- Alternatives considered:
  - Open-source models (LLaMA, Mistral): Free but require more infrastructure
  - Anthropic Claude: High quality but costs may exceed free tier
  - Hugging Face: Good for open-source models but requires hosting

### Architecture Options

**Monolithic vs. Microservices Architecture**
- Decision: Separate frontend (Docusaurus) and backend (FastAPI) but keep RAG services in one backend API
- Rationale: Separating concerns while keeping the architecture simple. Frontend handles static content delivery, backend handles dynamic RAG processing.
- Alternatives considered:
  - Full microservices: More complexity than needed for this project
  - Pure monolithic: Would require using Python for frontend, reducing performance for static content

**Static vs. Dynamic Content Delivery**
- Decision: Static content (textbook chapters) via GitHub Pages, dynamic AI functionality via backend API
- Rationale: Cost-effective hosting for static content with dedicated backend for AI processing
- Alternatives considered:
  - Fully dynamic: Higher hosting costs, slower loading
  - Static with client-side AI: Not feasible for RAG implementation

### Third-Party Services

**GitHub Pages Hosting**
- Decision: Host static Docusaurus site on GitHub Pages
- Rationale: Completely free, integrates well with GitHub workflow, reliable, and CDN-enhanced
- Alternatives considered:
  - Netlify: Good alternative but GitHub Pages is native to GitHub
  - Vercel: Good but GitHub Pages is sufficient for static content

**Embedding Models**
- Decision: Use OpenAI's text-embedding-ada-002 as the primary embedding model
- Rationale: High quality embeddings, well-maintained, good integration with LangChain
- Alternatives considered:
  - Sentence Transformers: Good free alternative, fallback option
  - Cohere embeddings: Quality alternative but less integration

## Technical Decisions

1. **Frontend Framework**: Docusaurus for static textbook content
2. **Backend Framework**: FastAPI for RAG API services
3. **Vector Database**: Qdrant for embedding storage
4. **Metadata Database**: Neon Postgres for configuration and metadata
5. **AI/LLM Model**: OpenAI API with fallback to open-source models
6. **Embedding Model**: OpenAI text-embedding-ada-002 with fallback to Sentence Transformers
7. **Deployment**: Static site on GitHub Pages, backend on a free tier hosting platform

## Open Questions

- How to handle content updates to the textbook that would require vector database re-embedding?
- What specific fallback mechanisms for open-source models should be implemented to stay within free-tier costs?
- How to implement the optional Urdu translation functionality efficiently?
- What rate limiting and usage monitoring is needed to stay within free-tier constraints?

## References

- Docusaurus documentation: https://docusaurus.io/
- FastAPI documentation: https://fastapi.tiangolo.com/
- Qdrant documentation: https://qdrant.tech/
- LangChain documentation: https://python.langchain.com/
- Neon documentation: https://neon.tech/