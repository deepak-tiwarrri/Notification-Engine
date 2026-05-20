"""
Notification business logic service
"""
from sqlalchemy.orm import Session
from app.models.notification import Notification
from app.schemas.notification import NotificationCreate, NotificationUpdate
from typing import Optional, List


class NotificationService:
    """Service for managing notifications"""
    
    @staticmethod
    def create_notification(db: Session, notification: NotificationCreate) -> Notification:
        """Create a new notification in database"""
        db_notification = Notification(
            title=notification.title,
            message=notification.message,
            alert_type=notification.alert_type,
            user_id=notification.user_id
        )
        db.add(db_notification)
        db.commit()
        db.refresh(db_notification)
        return db_notification
    
    @staticmethod
    def get_notification(db: Session, notification_id: int) -> Optional[Notification]:
        """Get a single notification by ID"""
        return db.query(Notification).filter(Notification.id == notification_id).first()
    
    @staticmethod
    def get_notifications(db: Session, skip: int = 0, limit: int = 100) -> List[Notification]:
        """Get all notifications with pagination"""
        return db.query(Notification).offset(skip).limit(limit).all()
    
    @staticmethod
    def update_notification(
        db: Session,
        notification_id: int,
        notification_update: NotificationUpdate
    ) -> Optional[Notification]:
        """Update an existing notification"""
        db_notification = db.query(Notification).filter(Notification.id == notification_id).first()
        if not db_notification:
            return None
        
        update_data = notification_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_notification, key, value)
        
        db.add(db_notification)
        db.commit()
        db.refresh(db_notification)
        return db_notification
    
    @staticmethod
    def delete_notification(db: Session, notification_id: int) -> bool:
        """Delete a notification"""
        db_notification = db.query(Notification).filter(Notification.id == notification_id).first()
        if not db_notification:
            return False
        
        db.delete(db_notification)
        db.commit()
        return True
