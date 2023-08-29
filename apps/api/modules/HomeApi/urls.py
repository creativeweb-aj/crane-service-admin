from django.urls import path
from apps.api.modules.HomeApi import api

urlpatterns = [
    # APIs urls
    path('home/site-info', api.siteInfo, name="HomeApi.api.site_info"),
    path('home/working-days', api.workingDays, name="HomeApi.api.working_days"),
    path('home/social-links', api.socialLinks, name="HomeApi.api.social_links"),
    path('home/about', api.about, name="HomeApi.api.about"),
    path('home/services', api.services, name="HomeApi.api.services"),
    path('home/cranes', api.cranes, name="HomeApi.api.cranes"),
    path('home/projects', api.projects, name="HomeApi.api.projects"),
    path('home/testimonials', api.testimonials, name="HomeApi.api.testimonials"),
    path('home/add-message', api.addMessage, name="HomeApi.api.add_message")
]
