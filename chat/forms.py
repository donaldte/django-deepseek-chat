from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    """Formulaire de création et modification de projet"""
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nom du projet"
        })
    )

    class Meta:
        model = Project
        fields = ["name"]
