from django.urls import path
from . import views


urlpatterns = [
    # Social page
    path('social-page/', views.indexSocialPage, name="social_page.index"),
    path('social-page/add', views.addSocialPage, name="social_page.add"),
    path('social-page/update/<int:id>', views.updateSocialPage, name="social_page.update"),
    path('social-page/view/<int:id>/', views.viewSocialPage, name="social_page.view"),
    path('social-page/status/<int:id>/', views.statusSocialPage, name="social_page.status"),
    path('social-page/delete/<int:id>/', views.deleteSocialPage, name="social_page.delete"),
    # Social Link
    path('staff/', views.indexSocialLink, name="social_link.index"),
    path('staff/add', views.addSocialLink, name="social_link.add"),
    path('staff/update/<int:id>', views.updateSocialLink, name="social_link.update"),
    path('staff/view/<int:id>/', views.viewSocialLink, name="social_link.view"),
    path('staff/status/<int:id>/', views.statusSocialLink, name="social_link.status"),
    path('staff/delete/<int:id>/', views.deleteSocialLink, name="social_link.delete")
]
