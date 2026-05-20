"""
WebSocket endpoints for real-time alert streaming
"""
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.utils.websocket_manager import WebSocketManager

router = APIRouter()
manager = WebSocketManager()


@router.websocket("/connect/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    """
    WebSocket endpoint for real-time alert notifications
    """
    await manager.connect(websocket, client_id)
    try:
        while True:
            data = await websocket.receive_text()
            # Echo back or process received data
            await manager.broadcast(f"Client {client_id}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(client_id)
        await manager.broadcast(f"Client {client_id} left the chat")


@router.post("/broadcast")
async def broadcast_alert(message: str):
    """
    Broadcast alert to all connected clients
    """
    await manager.broadcast(message)
    return {"message": "Alert broadcasted"}
