"""
Notification request/response schemas using Pydantic
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class NotificationCreate(BaseModel):
    """Schema for creating a new notification"""
    title: str = Field(..., min_length=1, max_length=255)
    message: str = Field(..., min_length=1)
    alert_type: str = Field(...,
                            description="Type: info, warning, error, success")
    user_id: Optional[str] = None


class NotificationUpdate(BaseModel):
    """Schema for updating a notification"""
    title: Optional[str] = None
    message: Optional[str] = None
    alert_type: Optional[str] = None
    is_read: Optional[bool] = None


class NotificationResponse(BaseModel):
    """Schema for notification response"""
    id: int
    title: str
    message: str
    alert_type: str
    user_id: Optional[str]
    is_read: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
