import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Company, CompanyMembership, CompanyUpdate

class CompanyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.company_id = self.scope["url_route"]["kwargs"]["company_id"]
        self.group_name = f"company_{self.company_id}"

        if not self.scope["user"].is_authenticated:
            await self.close()
            return

        is_member = await self.check_membership()
        if not is_member:
            await self.close()
            return

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]

        await self.save_update(message)

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "company_message",
                "message": message,
                "user": self.scope["user"].username
            }
        )

    async def company_message(self, event):
        await self.send(text_data=json.dumps({
            "user": event["user"],
            "message": event["message"]
        }))

    @database_sync_to_async
    def check_membership(self):
        return CompanyMembership.objects.filter(
            user=self.scope["user"],
            company_id=self.company_id
        ).exists()

    @database_sync_to_async
    def save_update(self, text):
        return CompanyUpdate.objects.create(
            company_id=self.company_id,
            text=text
        )
