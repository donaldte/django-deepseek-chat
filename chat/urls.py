from django.urls import path
from .views import ProjectManageView, ProjectUpdateView, ProjectDeleteView, ChatView, ChatMessageView

urlpatterns = [
    path("", ProjectManageView.as_view(), name="project_list"),
    path("projects/update/<int:pk>/", ProjectUpdateView.as_view(), name="project_update"),
    path("projects/delete/<int:pk>/", ProjectDeleteView.as_view(), name="project_delete"),
]
