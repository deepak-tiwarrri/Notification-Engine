"""
FastAPI application initialization and middleware configuration
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import engine, Base
from app.models.notification import Notification
from app.routes import http_alerts, ws_alerts

# Create tables on startup
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include routers
app.include_router(http_alerts.router, prefix="/api/alerts", tags=["alerts"])
app.include_router(ws_alerts.router, prefix="/ws", tags=["websocket"])


@app.get("/")
def read_root():
    """Health check endpoint"""
    return {"message": "Notification Engine API is running"}


@app.get("/health")
def health_check():
    """Detailed health check"""
    return {"status": "healthy", "app": settings.APP_NAME}
