from django.urls import path
from . import views


urlpatterns = [
    # Staff Urls
    path('staff/', views.indexStaff, name="staff.index"),
    path('staff/add', views.addStaff, name="staff.add"),
    path('staff/update/<int:id>', views.updateStaff, name="staff.update"),
    path('staff/status/<int:id>', views.statusStaff, name="staff.status"),
    path('staff/delete/<int:id>', views.deleteStaff, name="staff.delete")
]
