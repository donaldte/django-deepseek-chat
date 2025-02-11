from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomSignupForm(UserCreationForm):
    """Formulaire d'inscription personnalisé"""
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control", 
            "placeholder": "Nom d'utilisateur",
            "hx-post": "/compte/check-username/",  # Vérification en temps réel
            "hx-trigger": "keyup delay:500ms",
            "hx-target": "#username-feedback"
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", 
                                       "placeholder": "Email"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control",
                                          "placeholder": "Mot de passe"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control",
                                          "placeholder": "Confirmez le mot de passe"})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class CustomLoginForm(AuthenticationForm):
    """Formulaire de connexion personnalisé"""
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control",
                                      "placeholder": "Nom d'utilisateur"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control",
                                          "placeholder": "Mot de passe"})
    )


class ProfileUpdateForm(forms.ModelForm):
    """Formulaire de mise à jour du profil utilisateur"""
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control",
                                      "placeholder": "Nom d'utilisateur"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control",
                                       "placeholder": "Email"})
    )

    class Meta:
        model = User
        fields = ["username", "email"]
