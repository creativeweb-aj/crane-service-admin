from django.urls import path
from . import views


urlpatterns = [
    # About
    path('about/', views.indexAbout, name="about.index"),
    path('about/add', views.addAbout, name="about.add"),
    path('about/update/<int:id>', views.updateAbout, name="about.update"),
    path('about/view/<int:id>/', views.viewAbout, name="about.view"),
    path('about/status/<int:id>/', views.statusAbout, name="about.status"),
    path('about/delete/<int:id>/', views.deleteAbout, name="about.delete"),
    # Key Point
    path('key-point/', views.indexKeyPoint, name="keypoint.index"),
    path('key-point/add', views.addKeyPoint, name="keypoint.add"),
    path('key-point/update/<int:id>', views.updateKeyPoint, name="keypoint.update"),
    path('key-point/view/<int:id>/', views.viewKeyPoint, name="keypoint.view"),
    path('key-point/status/<int:id>/', views.statusKeyPoint, name="keypoint.status"),
    path('key-point/delete/<int:id>/', views.deleteKeyPoint, name="keypoint.delete"),
    # Key Point
    path('our-value/', views.indexOurValue, name="our_value.index"),
    path('our-value/add', views.addOurValue, name="our_value.add"),
    path('our-value/update/<int:id>', views.updateOurValue, name="our_value.update"),
    path('our-value/view/<int:id>/', views.viewOurValue, name="our_value.view"),
    path('our-value/status/<int:id>/', views.statusOurValue, name="our_value.status"),
    path('our-value/delete/<int:id>/', views.deleteOurValue, name="our_value.delete"),
    # Person
    path('person/', views.indexPerson, name="person.index"),
    path('person/add', views.addPerson, name="person.add"),
    path('person/update/<int:id>', views.updatePerson, name="person.update"),
    path('person/view/<int:id>/', views.viewPerson, name="person.view"),
    path('person/status/<int:id>/', views.statusPerson, name="person.status"),
    path('person/delete/<int:id>/', views.deletePerson, name="person.delete"),
    # Working Day
    path('working-day/', views.indexWorkingDay, name="working_day.index"),
    path('working-day/add', views.addWorkingDay, name="working_day.add"),
    path('working-day/update/<int:id>', views.updateWorkingDay, name="working_day.update"),
    path('working-day/view/<int:id>/', views.viewWorkingDay, name="working_day.view"),
    path('working-day/status/<int:id>/', views.statusWorkingDay, name="working_day.status"),
    path('working-day/delete/<int:id>/', views.deleteWorkingDay, name="working_day.delete"),
]
