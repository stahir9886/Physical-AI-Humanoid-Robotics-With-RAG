# Data Model: AI-Native Physical AI & Humanoid Robotics Textbook

**Feature**: textbook-generation
**Date**: 2025-12-10
**Spec**: [Link to spec.md]

## Overview

This document defines the data models for the AI-native textbook with RAG chatbot. Since the system primarily handles static textbook content with dynamic AI interactions, the data model includes entities for content management, user interactions, and system configuration.

## Entities

### Textbook Chapter
- **ID**: Unique identifier for the chapter
- **Title**: String, required, max 255 characters
- **Content**: Text, required, contains the chapter content in markdown format
- **Chapter Number**: Integer, required, order of the chapter in the textbook
- **Language**: String, default "en", for potential multilingual support
- **Created Date**: Timestamp
- **Updated Date**: Timestamp
- **Status**: Enum (Draft, Published, Archived), default "Published"

**Validation Rules**:
- Chapter Number must be unique within the textbook
- Title and Content are required fields
- Chapter Number must be positive

### User Session
- **Session ID**: Unique identifier for the session
- **User ID**: Foreign key to user, nullable (for anonymous users)
- **Start Time**: Timestamp, required
- **End Time**: Timestamp, nullable
- **IP Address**: String, for rate limiting
- **User Agent**: Text, for analytics

**Validation Rules**:
- Start Time is required
- End Time must be after Start Time if provided

### Chat Query
- **Query ID**: Unique identifier for the query
- **Session ID**: Foreign key to User Session, required
- **Query Text**: Text, required
- **Timestamp**: Timestamp, required
- **Source Chapter**: Foreign key to Textbook Chapter, nullable

**Validation Rules**:
- Query Text is required
- Timestamp is required
- Session ID is required

### Chat Response
- **Response ID**: Unique identifier for the response
- **Query ID**: Foreign key to Chat Query, required
- **Response Text**: Text, required
- **Timestamp**: Timestamp, required
- **Confidence Score**: Float (0.0-1.0), nullable
- **Source Documents**: JSON array of document references, nullable

**Validation Rules**:
- Query ID is required
- Response Text is required
- Timestamp is required

### User Profile
- **User ID**: Unique identifier for the user
- **Email**: String, unique, nullable
- **Preferences**: JSON, for storing user settings (language, etc.)
- **Created Date**: Timestamp
- **Last Active**: Timestamp

**Validation Rules**:
- Email must be unique if provided

### Language Setting
- **Setting ID**: Unique identifier
- **Language Code**: String, required (e.g., "en", "ur")
- **Language Name**: String, required (e.g., "English", "Urdu")
- **Content Available**: Boolean, default false
- **Interface Available**: Boolean, default true

**Validation Rules**:
- Language Code and Name are required
- Language Code must follow ISO 639-1 or 639-2 standards

### Personalized Chapter View
- **View ID**: Unique identifier
- **User ID**: Foreign key to User Profile, required
- **Chapter ID**: Foreign key to Textbook Chapter, required
- **Bookmarks**: JSON array of positions, nullable
- **Highlights**: JSON array of text ranges, nullable
- **Annotations**: JSON array of user notes, nullable
- **Last Viewed**: Timestamp

**Validation Rules**:
- User ID and Chapter ID are required
- Must have a unique constraint on (User ID, Chapter ID)

## Relationships

1. **Textbook Chapter** → (1 to many) → **Chat Query** (via Source Chapter)
2. **User Session** → (1 to many) → **Chat Query** (via Session ID)
3. **Chat Query** → (1 to 1) → **Chat Response** (via Query ID)
4. **User Profile** → (1 to many) → **User Session** (via User ID)
5. **User Profile** → (1 to many) → **Personalized Chapter View** (via User ID)
6. **Textbook Chapter** → (1 to many) → **Personalized Chapter View** (via Chapter ID)

## State Transitions

**Textbook Chapter**:
- Draft → Published (when content is approved)
- Published → Archived (when chapter is deprecated)

## Additional Notes

- Textbook content is primarily stored in markdown files, with metadata in the database
- RAG embeddings are stored separately in the Qdrant vector database
- User personalization data is stored in the database but only for registered users
- For anonymous users, personalization features are limited to browser storage