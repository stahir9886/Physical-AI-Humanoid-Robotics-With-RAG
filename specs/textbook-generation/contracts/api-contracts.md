# API Contracts: AI-Native Physical AI & Humanoid Robotics Textbook

**Feature**: textbook-generation
**Date**: 2025-12-10
**Spec**: [Link to spec.md]

## OpenAPI Specification

```yaml
openapi: 3.0.3
info:
  title: Textbook RAG API
  description: API for the AI-Native Physical AI & Humanoid Robotics Textbook with RAG functionality
  version: 1.0.0
servers:
  - url: https://textbook-api.example.com
    description: Production server
  - url: https://dev-textbook-api.example.com
    description: Development server

paths:
  /api/chapters:
    get:
      summary: Get list of all textbook chapters
      description: Retrieve all published chapters with metadata
      parameters:
        - name: language
          in: query
          description: Language code for content (e.g., 'en', 'ur')
          required: false
          schema:
            type: string
            default: 'en'
      responses:
        '200':
          description: List of textbook chapters
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Chapter'
        '400':
          description: Invalid language parameter
        '500':
          description: Internal server error

  /api/chapters/{chapterId}:
    get:
      summary: Get specific chapter content
      description: Retrieve the content of a specific chapter by ID
      parameters:
        - name: chapterId
          in: path
          required: true
          description: Unique identifier of the chapter
          schema:
            type: string
      responses:
        '200':
          description: Chapter content retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Chapter'
        '404':
          description: Chapter not found
        '500':
          description: Internal server error

  /api/chat/query:
    post:
      summary: Submit a query to the RAG system
      description: Submit a question about the textbook content and receive an AI-generated response based solely on textbook content
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ChatRequest'
      responses:
        '200':
          description: AI response to the query
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChatResponse'
        '400':
          description: Invalid query or session
        '429':
          description: Rate limit exceeded
        '500':
          description: Internal server error

  /api/users/profile:
    get:
      summary: Get user profile
      description: Retrieve the current user's profile information and preferences
      responses:
        '200':
          description: User profile retrieved
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserProfile'
        '401':
          description: User not authenticated
        '500':
          description: Internal server error
    put:
      summary: Update user profile
      description: Update the current user's profile information and preferences
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserProfileUpdate'
      responses:
        '200':
          description: Profile updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserProfile'
        '400':
          description: Invalid profile data
        '401':
          description: User not authenticated
        '500':
          description: Internal server error

  /api/personalization/chapter/{chapterId}:
    get:
      summary: Get personalized chapter view
      description: Retrieve personalization data for a specific chapter (bookmarks, highlights, annotations)
      parameters:
        - name: chapterId
          in: path
          required: true
          description: Unique identifier of the chapter
          schema:
            type: string
      responses:
        '200':
          description: Personalized view retrieved
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PersonalizedChapterView'
        '401':
          description: User not authenticated
        '404':
          description: Chapter or personalization data not found
        '500':
          description: Internal server error
    post:
      summary: Update personalized chapter view
      description: Save personalization data for a specific chapter (bookmarks, highlights, annotations)
      parameters:
        - name: chapterId
          in: path
          required: true
          description: Unique identifier of the chapter
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PersonalizedChapterView'
      responses:
        '200':
          description: Personalized view updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PersonalizedChapterView'
        '400':
          description: Invalid personalization data
        '401':
          description: User not authenticated
        '500':
          description: Internal server error

components:
  schemas:
    Chapter:
      type: object
      required:
        - id
        - title
        - content
        - chapterNumber
        - language
        - status
      properties:
        id:
          type: string
          description: Unique identifier for the chapter
          example: "chapter-1-intro-physical-ai"
        title:
          type: string
          description: Title of the chapter
          example: "Introduction to Physical AI"
        content:
          type: string
          description: Chapter content in markdown format
          example: "# Introduction to Physical AI\nPhysical AI..."
        chapterNumber:
          type: integer
          description: Order of the chapter in the textbook
          example: 1
        language:
          type: string
          description: Language code for the content
          example: "en"
        status:
          type: string
          enum: [Draft, Published, Archived]
          description: Status of the chapter
          example: "Published"
        createdDate:
          type: string
          format: date-time
          description: Timestamp when the chapter was created
        updatedDate:
          type: string
          format: date-time
          description: Timestamp when the chapter was last updated

    ChatRequest:
      type: object
      required:
        - query
        - sessionId
      properties:
        query:
          type: string
          description: The user's question about the textbook content
          example: "What is the main principle of Physical AI?"
        sessionId:
          type: string
          description: Unique identifier for the user session
          example: "session-abc123"
        sourceChapterId:
          type: string
          description: Optional ID of chapter where query originated
          example: "chapter-1-intro-physical-ai"

    ChatResponse:
      type: object
      required:
        - queryId
        - response
        - timestamp
      properties:
        queryId:
          type: string
          description: ID of the original query
          example: "query-xyz789"
        response:
          type: string
          description: AI-generated response based on textbook content
          example: "Physical AI is a field that combines physical systems with artificial intelligence..."
        timestamp:
          type: string
          format: date-time
          description: Time when response was generated
        confidenceScore:
          type: number
          format: float
          minimum: 0.0
          maximum: 1.0
          description: Confidence score of the AI response
        sources:
          type: array
          items:
            type: string
          description: List of source document IDs used to generate response
          example: ["chapter-1-intro-physical-ai", "chapter-2-basics-humanoid"]

    UserProfile:
      type: object
      properties:
        userId:
          type: string
          description: Unique identifier for the user
          example: "user-123"
        email:
          type: string
          format: email
          description: User's email address
          example: "student@example.com"
        preferences:
          type: object
          description: User preferences and settings
          properties:
            language:
              type: string
              description: Preferred language for textbook content
              example: "en"
            interfaceLanguage:
              type: string
              description: Preferred language for UI elements
              example: "en"

    UserProfileUpdate:
      type: object
      properties:
        email:
          type: string
          format: email
          description: User's email address
          example: "student@example.com"
        preferences:
          type: object
          description: User preferences and settings
          properties:
            language:
              type: string
              description: Preferred language for textbook content
              example: "en"
            interfaceLanguage:
              type: string
              description: Preferred language for UI elements
              example: "en"

    PersonalizedChapterView:
      type: object
      properties:
        userId:
          type: string
          description: Unique identifier for the user
          example: "user-123"
        chapterId:
          type: string
          description: Unique identifier for the chapter
          example: "chapter-1-intro-physical-ai"
        bookmarks:
          type: array
          items:
            type: object
            properties:
              position:
                type: integer
                description: Position in the text
              label:
                type: string
                description: Optional label for the bookmark
          description: List of bookmarked positions in the chapter
        highlights:
          type: array
          items:
            type: object
            properties:
              start:
                type: integer
                description: Start position of the highlighted text
              end:
                type: integer
                description: End position of the highlighted text
              note:
                type: string
                description: Optional note about the highlight
          description: List of highlighted text ranges in the chapter
        annotations:
          type: array
          items:
            type: object
            properties:
              position:
                type: integer
                description: Position in the text where annotation applies
              content:
                type: string
                description: Content of the user annotation
          description: List of user annotations in the chapter
        lastViewed:
          type: string
          format: date-time
          description: Timestamp of last viewing

  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

security:
  - BearerAuth: []
```

## Summary of Endpoints

1. **GET /api/chapters** - Retrieve list of all textbook chapters
2. **GET /api/chapters/{chapterId}** - Retrieve specific chapter content
3. **POST /api/chat/query** - Submit a query to the RAG system
4. **GET/PUT /api/users/profile** - Manage user profile and preferences
5. **GET/POST /api/personalization/chapter/{chapterId}** - Manage personalization data for chapters

## Security & Rate Limiting

- Authentication required for personalization features
- Rate limiting implemented to ensure free-tier cost management
- Anonymous sessions tracked by session ID with limited personalization