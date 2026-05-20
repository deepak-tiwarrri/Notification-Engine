# Notification Engine - Backend Setup

This is the backend for the Notification Engine application, built with FastAPI and PostgreSQL.

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── config.py              # Environment variables & settings (Pydantic)
│   ├── database.py            # SQLAlchemy engine and session setup
│   ├── main.py                # FastAPI app initialization & middleware
│   ├── models/
│   │   ├── __init__.py
│   │   └── notification.py    # Database models
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── notification.py    # Pydantic validation schemas
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── http_alerts.py     # REST API endpoints
│   │   └── ws_alerts.py       # WebSocket endpoints
│   ├── services/
│   │   ├── __init__.py
│   │   └── notification.py    # Business logic layer
│   └── utils/
│       ├── __init__.py
│       └── websocket_manager.py  # WebSocket connection management
├── alembic/                   # Database migrations
├── venv/                      # Virtual environment
├── .env                       # Environment variables (secret)
├── alembic.ini                # Alembic configuration
├── requirements.txt           # Project dependencies
└── README.md                  # This file
```

## Setup Instructions

### 1. Create and Activate Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Edit the `.env` file with your actual database credentials and settings.

### 4. Initialize Database

```bash
# Create initial migration
alembic revision --autogenerate -m "Initial migration"

# Apply migration
alembic upgrade head
```

### 5. Run the Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, visit:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Key Features

- **FastAPI**: Modern, fast web framework
- **SQLAlchemy**: ORM for database operations
- **Pydantic**: Data validation and schema management
- **WebSocket**: Real-time alert broadcasting
- **PostgreSQL**: Robust database backend
- **Alembic**: Database migration management

## API Endpoints

### REST Endpoints

- `POST /api/alerts` - Create a new alert
- `GET /api/alerts` - Get all alerts (with pagination)
- `GET /api/alerts/{alert_id}` - Get specific alert
- `PUT /api/alerts/{alert_id}` - Update alert
- `DELETE /api/alerts/{alert_id}` - Delete alert

### WebSocket Endpoints

- `WS /ws/connect/{client_id}` - Connect to real-time alerts
- `POST /ws/broadcast` - Broadcast message to all clients

### Health Check

- `GET /` - Health check
- `GET /health` - Detailed health status

## Development Notes

- Ensure PostgreSQL is running before starting the application
- Update `.env` with actual database credentials
- Use `pip freeze > requirements.txt` to update dependencies
- Database tables are created automatically on app startup
