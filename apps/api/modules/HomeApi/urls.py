from django.urls import path
from apps.api.modules.HomeApi import api

urlpatterns = [
    # APIs urls
    path('home/site-details', api.siteDetails, name="HomeApi.api.site_details")
]
