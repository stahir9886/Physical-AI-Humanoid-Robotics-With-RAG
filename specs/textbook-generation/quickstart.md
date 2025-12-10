# Quickstart Guide: AI-Native Physical AI & Humanoid Robotics Textbook

**Feature**: textbook-generation
**Date**: 2025-12-10
**Spec**: [Link to spec.md]

## Purpose

This quickstart guide provides the minimal steps to get the AI-native textbook with RAG chatbot feature working end-to-end for development and testing.

## Prerequisites

- Node.js 18+ (for Docusaurus frontend)
- Python 3.11+ (for backend services)
- Docker (for local Qdrant and Neon development)
- An OpenAI API key (or setup for open-source alternatives)
- Git

## Setup Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install frontend dependencies:
   ```bash
   cd docusaurus
   npm install
   ```

3. Install backend dependencies:
   ```bash
   cd ../backend
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   # In the backend directory
   cp .env.example .env
   # Edit .env and add your OpenAI API key and other configuration
   ```

5. Start Qdrant for vector storage:
   ```bash
   docker run -d --name qdrant-container -p 6333:6333 qdrant/qdrant
   ```

6. Run the backend service:
   ```bash
   cd backend
   python -m src.api.main
   ```

7. In a separate terminal, run the frontend:
   ```bash
   cd docusaurus
   npm start
   ```

## Verification

1. Navigate to `http://localhost:3000` in your browser
2. Verify that the textbook chapters are displayed correctly
3. Test the RAG chatbot by asking a question about the textbook content
4. Verify that the response is generated and references the textbook content
5. Check that the response clearly states it's based on the textbook content and doesn't hallucinate information

## Common Issues

- If the backend service won't start, ensure Qdrant is running and accessible
- If chatbot responses are slow, check your OpenAI API key and rate limits
- If the frontend can't connect to the backend, check CORS settings in the backend configuration
- If embeddings are not working, verify that the content was properly indexed in Qdrant during setup