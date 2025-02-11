from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Project
from .forms import ProjectForm


class ProjectListView(LoginRequiredMixin, ListView):
    """Affiche la liste des projets de l'utilisateur"""
    model = Project
    template_name = "chat/project_list.html"
    context_object_name = "projects"

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user).order_by("-created_at")


class ProjectCreateView(LoginRequiredMixin, CreateView):
    """Vue pour créer un projet"""
    model = Project
    form_class = ProjectForm
    template_name = "chat/project_form.html"
    success_url = reverse_lazy("chat:project_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Projet créé avec succès 🎉")
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    """Permet de modifier un projet"""
    model = Project
    form_class = ProjectForm
    template_name = "chat/project_form.html"
    success_url = reverse_lazy("chat:project_list")

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Projet mis à jour avec succès ✅")
        return super().form_valid(form)


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    """Permet de supprimer un projet"""
    model = Project
    template_name = "chat/project_confirm_delete.html"
    success_url = reverse_lazy("chat:project_list")

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Projet supprimé avec succès ❌")
        return super().delete(request, *args, **kwargs)


class ChatView(LoginRequiredMixin, View):
    """Vue pour afficher les messages d'un projet"""
    template_name = "chat/chat.html"

    def get(self, request, project_id):
        project = get_object_or_404(Project, id=project_id, user=request.user)
        messages = project.chatmessage_set.all().order_by("timestamp")
        projects = Project.objects.filter(user=request.user).order_by("-created_at")
        return render(request, self.template_name, {"project": project, "messages_chat": messages, "projects": projects}) 
    
