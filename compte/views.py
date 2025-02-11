from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import CustomSignupForm, CustomLoginForm, ProfileUpdateForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupView(CreateView):
    """Vue pour l'inscription"""
    form_class = CustomSignupForm
    template_name = "compte/signup.html"
    success_url = reverse_lazy("chat:project_list")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)


class CustomLoginView(LoginView):
    """Vue pour la connexion"""
    authentication_form = CustomLoginForm
    template_name = "compte/login.html"


def logout_view(request):
    """Vue pour la déconnexion"""
    logout(request)
    return redirect("compte:login")




def check_username(request):
    """Vérifie si le nom d'utilisateur est déjà pris (HTMX)"""
    username = request.GET.get("username", None)
    if username and User.objects.filter(username=username).exists():
        return JsonResponse({"message": "Ce nom d'utilisateur est déjà pris"}, status=400)
    return JsonResponse({"message": "Nom d'utilisateur disponible"}, status=200)
