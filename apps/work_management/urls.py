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
    path('customer/delete/<int:id>', views.deleteCustomer, name="customer.delete"),
    # Work Urls
    path('work/', views.indexWork, name="work.index"),
    path('work/add', views.addWork, name="work.add"),
    path('work/view/<int:id>', views.viewWork, name="work.view"),
    path('work/update/<int:id>', views.updateWork, name="work.update"),
    path('work/status/<int:id>', views.statusWork, name="work.status"),
    path('work/complete-status/<int:id>', views.statusWorkComplete, name="work.status-complete"),
    path('work/delete/<int:id>', views.deleteWork, name="work.delete")
]
