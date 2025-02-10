from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path("ws/chat/<int:project_id>/", ChatConsumer.as_asgi()),
]
