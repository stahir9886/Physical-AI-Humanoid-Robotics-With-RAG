from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from src.models.chapter import TextbookChapter

router = APIRouter()

# This is a mock implementation for deployment
# In a real implementation, this would fetch from database
MOCK_CHAPTERS = [
    TextbookChapter(
        id="chapter-1-intro-physical-ai",
        title="Introduction to Physical AI",
        content="# Introduction to Physical AI\n\nPhysical AI is a field that combines physical systems with artificial intelligence...",
        chapter_number=1
    ),
    TextbookChapter(
        id="chapter-2-basics-humanoid",
        title="Basics of Humanoid Robotics",
        content="# Basics of Humanoid Robotics\n\nHumanoid robotics is a branch of robotics focused on creating robots with human-like characteristics...",
        chapter_number=2
    )
]

@router.get("/chapters", response_model=List[TextbookChapter])
async def get_chapters(
    language: str = Query("en", description="Language code for content")
):
    """
    Retrieve all published chapters with metadata.
    """
    # In production, this would fetch from database
    return MOCK_CHAPTERS


@router.get("/chapters/{chapter_id}", response_model=TextbookChapter)
async def get_chapter(chapter_id: str):
    """
    Retrieve the content of a specific chapter by ID.
    """
    # In production, this would fetch from database
    for chapter in MOCK_CHAPTERS:
        if chapter.id == chapter_id:
            return chapter
    
    raise HTTPException(status_code=404, detail="Chapter not found")