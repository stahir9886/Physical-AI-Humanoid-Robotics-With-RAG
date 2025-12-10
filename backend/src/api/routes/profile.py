from fastapi import APIRouter
from typing import Optional
from src.models.user import UserProfile

router = APIRouter()

# Mock user profile for deployment
MOCK_PROFILE = UserProfile(
    user_id="user-123",
    email="student@example.com",
    preferences={"language": "en", "interfaceLanguage": "en"}
)

@router.get("/users/profile", response_model=UserProfile)
async def get_profile():
    """
    Retrieve the current user's profile information and preferences.
    """
    # In production, this would fetch from database based on authentication
    return MOCK_PROFILE


@router.put("/users/profile", response_model=UserProfile)
async def update_profile(profile: UserProfile):
    """
    Update the current user's profile information and preferences.
    """
    # In production, this would update the database
    # For now, just return the updated profile
    return profile