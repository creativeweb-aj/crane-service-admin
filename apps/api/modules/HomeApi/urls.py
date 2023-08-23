from django.urls import path
from apps.api.modules.HomeApi import api

urlpatterns = [
    # APIs urls
    path('home/site-details', api.siteDetails, name="HomeApi.api.site_details"),
    path('home/about', api.about, name="HomeApi.api.about"),
    path('home/services', api.services, name="HomeApi.api.services"),
    path('home/projects', api.projects, name="HomeApi.api.projects"),
    path('home/testimonials', api.testimonials, name="HomeApi.api.testimonials"),
    path('home/add-message', api.addMessage, name="HomeApi.api.add_message")
]
