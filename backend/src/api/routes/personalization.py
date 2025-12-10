from fastapi import APIRouter
from src.models.personalization import PersonalizedChapterView

router = APIRouter()

# Mock personalization for deployment
MOCK_PERSONALIZATION = PersonalizedChapterView(
    userId="user-123",
    chapterId="chapter-1-intro-physical-ai",
    bookmarks=[],
    highlights=[],
    annotations=[]
)

@router.get("/personalization/chapter/{chapter_id}", response_model=PersonalizedChapterView)
async def get_personalization(chapter_id: str):
    """
    Retrieve personalization data for a specific chapter.
    """
    # In production, this would fetch from database based on authenticated user
    MOCK_PERSONALIZATION.chapterId = chapter_id
    return MOCK_PERSONALIZATION


@router.post("/personalization/chapter/{chapter_id}", response_model=PersonalizedChapterView)
async def update_personalization(chapter_id: str, personalization: PersonalizedChapterView):
    """
    Save personalization data for a specific chapter.
    """
    # In production, this would save to database
    personalization.chapterId = chapter_id
    return personalization