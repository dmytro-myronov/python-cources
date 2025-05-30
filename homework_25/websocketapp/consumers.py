# websocketapp/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Добавляем пользователя в группу
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Убираем пользователя из группы
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Получаем сообщение от WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        # Отправляем сообщение группе
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Получаем сообщение от группы
    async def chat_message(self, event):
        message = event['message']

        # Отправляем сообщение клиенту
        await self.send(text_data=json.dumps({
            'message': message
        }))
