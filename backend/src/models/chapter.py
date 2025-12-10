from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class TextbookChapter(BaseModel):
    id: str
    title: str
    content: str
    chapter_number: int
    language: str = "en"
    created_date: Optional[datetime] = None
    updated_date: Optional[datetime] = None
    status: str = "Published"  # Draft, Published, Archived
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "chapter-1-intro-physical-ai",
                "title": "Introduction to Physical AI",
                "content": "# Introduction to Physical AI\nPhysical AI...",
                "chapter_number": 1,
                "language": "en",
                "status": "Published"
            }
        }