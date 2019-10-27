from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("<int:pk>/", views.project, name="project"),
    path('add', views.addProject, name="addProject"),
    path('insert', views.addProjectButton, name="addProjectButton"),
    path('<int:pk>/delete', views.rmProjectButton, name="rmProjectButton")
]