from django.contrib import admin
from .models import Project, ChatMessage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "created_at")
    search_fields = ("name", "user__username")

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ("user", "project", "message", "timestamp")
    search_fields = ("user__username", "message")
    list_filter = ("timestamp",)
