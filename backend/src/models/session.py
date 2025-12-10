from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserSession(BaseModel):
    session_id: str
    user_id: Optional[str] = None  # For anonymous users
    start_time: datetime
    end_time: Optional[datetime] = None
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "session_id": "session-abc123",
                "user_id": "user-123",
                "start_time": "2023-10-01T10:00:00Z",
                "ip_address": "192.168.1.1",
                "user_agent": "Mozilla/5.0..."
            }
        }