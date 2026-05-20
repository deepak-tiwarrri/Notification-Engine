"""
REST API endpoints for alerts/notifications
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.notification import NotificationCreate, NotificationResponse, NotificationUpdate
from app.services.notification import NotificationService

router = APIRouter()
notification_service = NotificationService()


@router.post("/", response_model=NotificationResponse)
def create_alert(
    notification: NotificationCreate,
    db: Session = Depends(get_db)
):
    """Create a new alert/notification"""
    return notification_service.create_notification(db, notification)


@router.get("/", response_model=List[NotificationResponse])
def get_alerts(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Get all alerts with pagination"""
    return notification_service.get_notifications(db, skip, limit)


@router.get("/{alert_id}", response_model=NotificationResponse)
def get_alert(
    alert_id: int,
    db: Session = Depends(get_db)
):
    """Get a specific alert by ID"""
    notification = notification_service.get_notification(db, alert_id)
    if not notification:
        raise HTTPException(status_code=404, detail="Alert not found")
    return notification


@router.put("/{alert_id}", response_model=NotificationResponse)
def update_alert(
    alert_id: int,
    notification_update: NotificationUpdate,
    db: Session = Depends(get_db)
):
    """Update an alert"""
    notification = notification_service.update_notification(
        db, alert_id, notification_update)
    if not notification:
        raise HTTPException(status_code=404, detail="Alert not found")
    return notification


@router.delete("/{alert_id}")
def delete_alert(
    alert_id: int,
    db: Session = Depends(get_db)
):
    """Delete an alert"""
    success = notification_service.delete_notification(db, alert_id)
    if not success:
        raise HTTPException(status_code=404, detail="Alert not found")
    return {"message": "Alert deleted successfully"}
