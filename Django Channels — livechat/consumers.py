"""WebSocket consumer for live classroom chat"""
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ClassroomChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("classroom", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("classroom", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            "classroom",
            {"type": "chat.message", "message": data['message']}
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({"message": event["message"]}))
