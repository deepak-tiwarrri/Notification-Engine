"""
WebSocket connection manager for handling connected clients
"""
from fastapi import WebSocket
from typing import Dict, List


class WebSocketManager:
    """Manages WebSocket connections and broadcasting"""

    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, client_id: str):
        """Accept new WebSocket connection"""
        await websocket.accept()
        if client_id not in self.active_connections:
            self.active_connections[client_id] = []
        self.active_connections[client_id].append(websocket)

    def disconnect(self, client_id: str):
        """Remove disconnected client"""
        if client_id in self.active_connections:
            del self.active_connections[client_id]

    async def broadcast(self, message: str):
        """Send message to all connected clients"""
        disconnected_clients = []

        for client_id, connection in self.active_connections.items():
            try:
                await connection.send_text(message)
            except Exception as e:
                print(f"Error sending message to {client_id}: {e}")
                disconnected_clients.append(client_id)

        # Clean up disconnected clients
        for client_id in disconnected_clients:
            self.disconnect(client_id)

    async def send_personal_message(self, message: str, client_id: str):
        """Send message to a specific client"""
        if client_id in self.active_connections:
            connection = self.active_connections[client_id]
            try:
                await connection.send_text(message)
            except Exception as e:
                print(f"Error sending personal message to {client_id}: {e}")
                self.disconnect(client_id)

    def get_active_connections_count(self) -> int:
        """Get number of active connections"""
        return len(self.active_connections)
