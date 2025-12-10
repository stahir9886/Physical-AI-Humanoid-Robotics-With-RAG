# Tasks: textbook-generation

**Input**: Design documents from `/specs/textbook-generation/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `docusaurus/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume web app structure - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure with backend, docusaurus, and docs directories per implementation plan
- [x] T002 Initialize Docusaurus project with npm in docusaurus/ directory
- [x] T003 [P] Initialize Python project with requirements.txt in backend/
- [x] T004 Set up .env.example file in backend/ with placeholders for API keys and configuration
- [x] T005 Create basic directory structure in backend/src/ (models/, services/, api/) per plan

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 [P] Set up Qdrant client and configuration in backend/src/services/rag_service.py
- [x] T007 [P] Set up Neon database connection in backend/src/services/database.py
- [x] T008 Create TextbookChapter model in backend/src/models/chapter.py
- [x] T009 Create UserSession model in backend/src/models/session.py
- [x] T010 Create ChatQuery and ChatResponse models in backend/src/models/chat.py
- [x] T011 Create UserProfile model in backend/src/models/user.py
- [x] T012 Set up FastAPI application structure in backend/src/api/main.py with CORS and error handling
- [x] T013 [P] Create configuration module for environment variables in backend/src/config.py
- [x] T014 [P] Set up logging infrastructure in backend/src/utils/logging.py
- [x] T015 Create content indexing script in backend/src/scripts/index_content.py
- [x] T016 [P] Set up embedding service using OpenAI API in backend/src/services/embedding_service.py
- [x] T017 [P] Create rate limiting middleware for free-tier compliance in backend/src/middleware/rate_limit.py
- [x] T018 Create Dockerfile for backend in backend/Dockerfile

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Student Learner (Priority: P1) 🎯 MVP

**Goal**: Enable students to browse textbook content and interact with the RAG chatbot which responds with information exclusively from the textbook content

**Independent Test**: System allows a student to browse the textbook content, navigate between chapters, and engage with the RAG chatbot which responds with information exclusively from the textbook content

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T019 [P] [US1] Contract test for GET /api/chapters endpoint in backend/tests/contract/test_chapters.py
- [ ] T020 [P] [US1] Contract test for GET /api/chapters/{chapterId} endpoint in backend/tests/contract/test_chapters.py
- [ ] T021 [P] [US1] Contract test for POST /api/chat/query endpoint in backend/tests/contract/test_chat.py
- [ ] T022 [P] [US1] Integration test for chapter navigation flow in backend/tests/integration/test_textbook_flow.py
- [ ] T023 [P] [US1] Integration test for RAG chatbot query flow in backend/tests/integration/test_chat_flow.py

### Implementation for User Story 1

- [ ] T024 [US1] Create TextbookService in backend/src/services/textbook_service.py
- [ ] T025 [US1] Create RAGService in backend/src/services/rag_service.py
- [ ] T026 [US1] Implement GET /api/chapters endpoint in backend/src/api/routes/chapters.py
- [ ] T027 [US1] Implement GET /api/chapters/{chapterId} endpoint in backend/src/api/routes/chapters.py
- [ ] T028 [US1] Implement POST /api/chat/query endpoint in backend/src/api/routes/chat.py
- [ ] T029 [US1] Add chapter content validation to ensure responses are from textbook only
- [ ] T030 [US1] Create basic Docusaurus sidebar with automatic generation in docusaurus/sidebars.js
- [ ] T031 [US1] Create basic chapter navigation components in docusaurus/src/components/Navigation/
- [ ] T032 [US1] Create basic chatbot UI component in docusaurus/src/components/Chatbot/
- [ ] T033 [US1] Integrate chatbot with API calls in docusaurus/src/components/Chatbot/
- [ ] T034 [US1] Implement basic responsive design for textbook pages in docusaurus/src/css/custom.css
- [ ] T035 [US1] Add content for 6 textbook chapters in docusaurus/docs/
- [ ] T036 [US1] Add initial textbook content to Qdrant vector storage via indexing script
- [ ] T037 [US1] Add validation to ensure chat responses are sourced only from textbook content

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Instructor/Teacher (Priority: P2)

**Goal**: Enable instructors to search for specific topics within the textbook content and potentially customize chapter views if the optional feature is implemented

**Independent Test**: System allows an instructor to search for specific topics within the textbook content and potentially customize chapter views if the optional feature is implemented

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T038 [P] [US2] Contract test for GET /api/users/profile endpoint in backend/tests/contract/test_profile.py
- [ ] T039 [P] [US2] Contract test for PUT /api/users/profile endpoint in backend/tests/contract/test_profile.py
- [ ] T040 [P] [US2] Contract test for GET /api/personalization/chapter/{chapterId} endpoint in backend/tests/contract/test_personalization.py
- [ ] T041 [P] [US2] Contract test for POST /api/personalization/chapter/{chapterId} endpoint in backend/tests/contract/test_personalization.py
- [ ] T042 [P] [US2] Integration test for instructor search flow in backend/tests/integration/test_instructor_flow.py

### Implementation for User Story 2

- [ ] T043 [P] [US2] Create LanguageSetting model in backend/src/models/language.py
- [ ] T044 [P] [US2] Create PersonalizedChapterView model in backend/src/models/personalization.py
- [ ] T045 [US2] Create UserService in backend/src/services/user_service.py
- [ ] T046 [US2] Create PersonalizationService in backend/src/services/personalization_service.py
- [ ] T047 [US2] Implement GET /api/users/profile endpoint in backend/src/api/routes/profile.py
- [ ] T048 [US2] Implement PUT /api/users/profile endpoint in backend/src/api/routes/profile.py
- [ ] T049 [US2] Implement GET /api/personalization/chapter/{chapterId} endpoint in backend/src/api/routes/personalization.py
- [ ] T050 [US2] Implement POST /api/personalization/chapter/{chapterId} endpoint in backend/src/api/routes/personalization.py
- [ ] T051 [US2] Add authentication middleware for protected routes in backend/src/middleware/auth.py
- [ ] T052 [US2] Create chapter personalization UI components in docusaurus/src/components/Personalization/
- [ ] T053 [US2] Integrate personalization features with API in docusaurus/src/components/Personalization/
- [ ] T054 [US2] Add search functionality across textbook content in backend/src/services/textbook_service.py
- [ ] T055 [US2] Create search UI component in docusaurus/src/components/Search/
- [ ] T056 [US2] Integrate search functionality in docusaurus/src/components/Search/

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Self-Learner (Priority: P3)

**Goal**: Enable self-learners to freely browse the content and interact with the RAG chatbot to enhance understanding of complex concepts

**Independent Test**: System allows a self-learner to freely browse the content and interact with the RAG chatbot to enhance understanding of complex concepts

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T057 [P] [US3] Contract test for anonymous session management in backend/tests/contract/test_sessions.py
- [ ] T058 [P] [US3] Integration test for anonymous user flow in backend/tests/integration/test_anonymous_flow.py
- [ ] T059 [P] [US3] Unit test for rate limiting functionality in backend/tests/unit/test_rate_limit.py

### Implementation for User Story 3

- [ ] T060 [US3] Update UserSession model to support anonymous users in backend/src/models/session.py
- [ ] T061 [US3] Update RAGService to handle anonymous sessions appropriately in backend/src/services/rag_service.py
- [ ] T062 [US3] Implement rate limiting for anonymous users in backend/src/middleware/rate_limit.py
- [ ] T063 [US3] Enhance chatbot UI for guest users in docusaurus/src/components/Chatbot/
- [ ] T064 [US3] Add analytics tracking for anonymous users in backend/src/services/analytics.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T065 [P] Documentation updates in docusaurus/docs/
- [ ] T066 [P] Backend API documentation with FastAPI auto-generated docs
- [ ] T067 [P] Unit tests for core services in backend/tests/unit/
- [ ] T068 [P] E2E tests for critical user flows in docusaurus/tests/e2e/
- [ ] T069 [P] Performance optimization for content loading
- [ ] T070 [P] Error handling and user feedback improvements
- [ ] T071 [P] Security hardening and input validation
- [ ] T072 [P] Internationalization setup for Urdu translation
- [ ] T073 [P] Build optimization for faster loading
- [ ] T074 Run quickstart.md validation in all environments

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
T019 [P] [US1] Contract test for GET /api/chapters endpoint in backend/tests/contract/test_chapters.py
T020 [P] [US1] Contract test for GET /api/chapters/{chapterId} endpoint in backend/tests/contract/test_chapters.py
T021 [P] [US1] Contract test for POST /api/chat/query endpoint in backend/tests/contract/test_chat.py

# Launch all models for User Story 1 together:
T024 [US1] Create TextbookService in backend/src/services/textbook_service.py
T025 [US1] Create RAGService in backend/src/services/rag_service.py
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence