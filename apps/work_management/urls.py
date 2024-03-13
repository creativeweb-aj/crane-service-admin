from django.urls import path
from . import views


urlpatterns = [
    # Staff Urls
    path('staff/', views.indexStaff, name="staff.index"),
    path('staff/add', views.addStaff, name="staff.add"),
    path('staff/update/<int:id>', views.updateStaff, name="staff.update"),
    path('staff/status/<int:id>', views.statusStaff, name="staff.status"),
    path('staff/delete/<int:id>', views.deleteStaff, name="staff.delete"),
    # Customer Urls
    path('customer/', views.indexCustomer, name="customer.index"),
    path('customer/add', views.addCustomer, name="customer.add"),
    path('customer/update/<int:id>', views.updateCustomer, name="customer.update"),
    path('customer/status/<int:id>', views.statusCustomer, name="customer.status"),
    path('customer/delete/<int:id>', views.deleteCustomer, name="customer.delete")
]
