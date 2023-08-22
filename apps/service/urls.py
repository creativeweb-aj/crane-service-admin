from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="service.index"),
    path('add', views.add, name="service.add"),
    path('update/<int:id>', views.update, name="service.update"),
    path('view/<int:id>/', views.view, name="service.view"),
    path('status/<int:id>/', views.status, name="service.status"),
    path('delete/<int:id>/', views.delete, name="service.delete"),
]
