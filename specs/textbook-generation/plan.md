# Implementation Plan: textbook-generation

**Branch**: `textbook-generation` | **Date**: 2025-12-10 | **Spec**: [Link to spec.md]
**Input**: Feature specification from `/specs/textbook-generation/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This plan implements an AI-native textbook for Physical AI & Humanoid Robotics with 6 chapters and a RAG (Retrieval Augmented Generation) chatbot. The textbook will be built using Docusaurus for static hosting on GitHub Pages, with a RAG backend using Qdrant for vector storage and Neon for the database, operating within free-tier costs. The system will allow users to browse content and interact with an AI chatbot that provides answers based exclusively on the textbook content.

## Technical Context

**Language/Version**: JavaScript/TypeScript (Node.js 18+ for Docusaurus), Python 3.11 (for backend services)
**Primary Dependencies**: Docusaurus, FastAPI, Qdrant, Neon Postgres, Langchain, OpenAI API or open-source LLM
**Storage**: Static content served via GitHub Pages, vector embeddings in Qdrant, configuration in Neon
**Testing**: Jest for frontend, pytest for backend, Playwright for E2E tests
**Target Platform**: Web-based application accessible on desktop, tablet, and mobile devices
**Project Type**: Web application (frontend + backend services)
**Performance Goals**: Page load under 3 seconds, chatbot response under 2 seconds for 95% of queries
**Constraints**: Must operate within free-tier costs of cloud services, no hallucinated responses from chatbot
**Scale/Scope**: Expected to handle up to 1000 concurrent users during academic semester periods

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Based on the Physical AI & Humanoid Robotics constitution:

**Simplicity**:
- ✓ The architecture uses standard web technologies (Docusaurus, FastAPI)
- ✓ RAG implementation is straightforward using Qdrant vector storage
- ❓ The dual frontend/backend structure needs to be justified against simpler alternatives (monolithic solution)

**Accuracy**:
- ✓ The design includes verification mechanisms to ensure AI responses are based on textbook content
- ✓ Content validation system will be implemented to maintain factual correctness

**Minimalism**:
- ✓ Using standard technologies avoids custom or complex solutions
- ✓ Core functionality limited to textbook delivery and RAG chatbot
- ❓ Optional features (Urdu translation, personalization) must be evaluated against minimalism principle

**Fast Builds**:
- ✓ Docusaurus static site generation should maintain reasonable build times
- ❓ Build performance will need monitoring as content grows

**Free-tier Architecture**:
- ✓ Architecture choices (Qdrant, Neon) support free-tier operation
- ✓ Static hosting through GitHub Pages ensures cost-effective delivery
- ✓ Resource constraints are considered in performance goals

**RAG Answers ONLY from Book Text**:
- ✓ Design includes content restriction mechanisms to prevent hallucination
- ✓ Vector storage will only contain textbook content
- ✓ Strict content filtering will be implemented in the RAG pipeline

**Constitution Violation Assessment**:
All principles are addressed in the design. The dual frontend/backend structure is justified by the need to separate static content delivery (Docusaurus/GitHub Pages) from dynamic RAG processing (backend services). Optional features will be implemented as modular additions that can be enabled/disabled based on requirements.

## Project Structure

### Documentation (this feature)

```text
specs/textbook-generation/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── models/
│   ├── services/
│   │   ├── rag_service.py
│   │   ├── embedding_service.py
│   │   └── textbook_service.py
│   └── api/
│       └── main.py
└── tests/
    ├── contract/
    ├── integration/
    └── unit/

frontend/
├── src/
│   ├── components/
│   │   ├── Chatbot/
│   │   ├── Textbook/
│   │   └── Navigation/
│   ├── pages/
│   └── services/
└── tests/
    ├── unit/
    └── e2e/

# For Docusaurus-based textbook with embedded chatbot
docusaurus/
├── src/
│   ├── components/
│   ├── pages/
│   └── theme/
└── docs/
    ├── chapter-1/
    ├── chapter-2/
    ├── chapter-3/
    ├── chapter-4/
    ├── chapter-5/
    └── chapter-6/
```

**Structure Decision**: The project will be structured as a web application with separate backend services for RAG functionality and a Docusaurus frontend for the textbook content. This allows for clear separation of concerns between static content delivery and dynamic AI interactions.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |