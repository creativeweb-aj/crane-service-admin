from django.urls import path
from . import views


urlpatterns = [
    # Crane
    path('crane/', views.craneIndex, name="crane.index"),
    path('crane/add', views.addCrane, name="crane.add"),
    path('crane/update/<int:id>', views.updateCrane, name="crane.update"),
    path('crane/view/<int:id>/', views.craneView, name="crane.view"),
    path('crane/status/<int:id>/', views.craneStatus, name="crane.status"),
    path('crane/delete/<int:id>/', views.craneDelete, name="crane.delete"),
    # Project
    path('project/', views.projectIndex, name="project.index"),
    path('project/add', views.addProject, name="project.add"),
    path('project/update/<int:id>', views.updateProject, name="project.update"),
    path('project/view/<int:id>/', views.projectView, name="project.view"),
    path('project/status/<int:id>/', views.projectStatus, name="project.status"),
    path('project/delete/<int:id>/', views.projectDelete, name="project.delete"),
]
