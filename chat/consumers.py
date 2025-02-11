import json
import ollama
import markdown2
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from .models import Project, ChatMessage
from asgiref.sync import sync_to_async

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """Accept WebSocket connection"""
        self.project_id = self.scope["url_route"]["kwargs"]["project_id"]
        self.room_group_name = f"chat_{self.project_id}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        """Handle WebSocket disconnection"""
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        """Receive a message and stream AI response"""
        data = json.loads(text_data)
        user_message = data["message"]

        # Send user message to frontend
        await self.send(text_data=json.dumps({"message": user_message, "sender": "user"}))

        # Get project
        project = await self.get_project(self.project_id)
        if not project:
            return

        # Stream AI response
        ai_response = ""
        raw_markdown_response = ""
        stream = ollama.chat(
            model="deepseek-r1:1.5b",
            messages=[{"role": "user", "content": user_message}],
            stream=True
        )

        for chunk in stream:
            raw_markdown_response += chunk["message"]["content"]
            formatted_html = markdown2.markdown(raw_markdown_response)

            # Send each chunk immediately
            await self.send(text_data=json.dumps({"message": formatted_html, "sender": "ai"}))
            await asyncio.sleep(0.05)  # Small delay to allow frontend to process

        # Save full AI response
        await self.save_message(project, self.scope["user"], user_message, formatted_html)

        # **Explicitly Close WebSocket After AI Response is Sent**
        await self.send(text_data=json.dumps({"close": True}))  # Notify frontend to close
        await self.close()  # Close WebSocket connection

    @sync_to_async
    def get_project(self, project_id):
        """Retrieve project synchronously inside async context"""
        try:
            return Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return None

    @sync_to_async
    def save_message(self, project, user, user_message, formatted_html):
        """Save the message in the database asynchronously"""
        ChatMessage.objects.create(
            project=project, user=user, message=user_message, response=formatted_html
        )
