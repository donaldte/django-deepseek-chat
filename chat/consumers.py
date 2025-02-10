import json
import ollama
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """Accepter la connexion WebSocket"""
        self.project_id = self.scope["url_route"]["kwargs"]["project_id"]
        self.room_group_name = f"chat_{self.project_id}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        """Déconnecter l'utilisateur"""
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        """Recevoir un message et envoyer la réponse en streaming"""
        data = json.loads(text_data)
        user_message = data["message"]

        # Envoyer le message utilisateur à l'interface
        await self.send(text_data=json.dumps({"message": user_message, "sender": "user"}))

        # Envoyer la réponse de DeepSeek en streaming
        ai_response = ""
        stream = ollama.chat(
            model="deepseek-r1:1.5b",
            messages=[{"role": "user", "content": user_message}],
            stream=True
        )

        for chunk in stream:
            ai_response += chunk["message"]["content"]
            await self.send(text_data=json.dumps({"message": ai_response, "sender": "ai"}))

        # Stocker la conversation dans la base de données
        from .models import Project, ChatMessage
        project = await self.get_project(self.project_id)
        if project:
            ChatMessage.objects.create(project=project, user=self.scope["user"], message=user_message, response=ai_response)

    async def get_project(self, project_id):
        """Récupérer le projet de manière asynchrone"""
        from django.contrib.auth import get_user_model
        from .models import Project
        User = get_user_model()
        try:
            return await Project.objects.aget(id=project_id)
        except Project.DoesNotExist:
            return None
