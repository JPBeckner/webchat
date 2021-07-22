from json import loads, dumps
from datetime import datetime

from channels.generic.websocket import AsyncWebsocketConsumer
from bot.views import check_bot_command


class ChatConsumer(AsyncWebsocketConsumer):
    # Connect to room
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    # Leave room group
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'room': self.room_name
            }
        )

    # Receive message from room group
    @check_bot_command
    async def chat_message(self, event):
        message = self.format_message(
            message=event['message'],
            username=event.get('username', 'TheUnknown')
        )

        # Send message to WebSocket
        await self.send(text_data=dumps({
            'message': message
        }))


    def format_message(self, message: str, username: str) -> str:
        return f"[{datetime.now().strftime('%H:%M:%S')}] {username}: {message}"
