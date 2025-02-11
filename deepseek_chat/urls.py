
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("compte/", include("compte.urls")),  # Inclure l'application compte
    path("", include("chat.urls")),  # Inclure l'application chat


]
