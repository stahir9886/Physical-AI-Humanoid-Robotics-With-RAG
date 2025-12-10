from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime


class UserProfile(BaseModel):
    user_id: str
    email: Optional[str] = None
    preferences: Optional[Dict[str, Any]] = {}
    created_date: Optional[datetime] = None
    last_active: Optional[datetime] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "user-123",
                "email": "student@example.com",
                "preferences": {
                    "language": "en",
                    "interfaceLanguage": "en"
                }
            }
        }