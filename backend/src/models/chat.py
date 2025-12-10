from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ChatQuery(BaseModel):
    query_id: str
    session_id: str
    query_text: str
    timestamp: datetime
    source_chapter_id: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "query_id": "query-xyz789",
                "session_id": "session-abc123",
                "query_text": "What is the main principle of Physical AI?",
                "timestamp": "2023-10-01T10:05:00Z",
                "source_chapter_id": "chapter-1-intro-physical-ai"
            }
        }


class ChatResponse(BaseModel):
    response_id: str
    query_id: str
    response_text: str
    timestamp: datetime
    confidence_score: Optional[float] = None  # 0.0 to 1.0
    source_documents: Optional[List[str]] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "response_id": "response-123",
                "query_id": "query-xyz789",
                "response_text": "Physical AI is a field that combines physical systems with artificial intelligence...",
                "timestamp": "2023-10-01T10:05:02Z",
                "confidence_score": 0.95,
                "source_documents": ["chapter-1-intro-physical-ai"]
            }
        }