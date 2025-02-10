from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Project

class ProjectManageView(LoginRequiredMixin, ListView, CreateView):
    """Affiche la liste des projets et permet d'en créer un"""
    model = Project
    template_name = "chat/project_list.html"
    context_object_name = "projects"
    fields = ["name"]
    success_url = reverse_lazy("project_list")

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user).order_by("-created_at")

    def form_valid(self, form):
        """Associer l'utilisateur au projet avant de le sauvegarder"""
        form.instance.user = self.request.user
        return super().form_valid(form)



class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    """Permet de modifier un projet"""
    model = Project
    fields = ["name"]
    template_name = "chat/project_form.html"
    success_url = reverse_lazy("project_list")

    def get_queryset(self):
        """Limiter la modification aux projets appartenant à l'utilisateur"""
        return Project.objects.filter(user=self.request.user)


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    """Permet de supprimer un projet"""
    model = Project
    template_name = "chat/project_confirm_delete.html"
    success_url = reverse_lazy("project_list")

    def get_queryset(self):
        """Limiter la suppression aux projets appartenant à l'utilisateur"""
        return Project.objects.filter(user=self.request.user)
