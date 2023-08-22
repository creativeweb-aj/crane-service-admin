from django.urls import path
from . import views


urlpatterns = [
    # Message
    path('message/', views.indexMessage, name="message.index"),
    path('message/view/<int:id>/', views.viewMessage, name="message.view"),
    path('message/delete/<int:id>/', views.deleteMessage, name="message.delete"),
    # Testimonial
    path('testimonial/', views.indexTestimonial, name="testimonial.index"),
    path('testimonial/add', views.addTestimonial, name="testimonial.add"),
    path('testimonial/update/<int:id>', views.updateTestimonial, name="testimonial.update"),
    path('testimonial/view/<int:id>/', views.viewTestimonial, name="testimonial.view"),
    path('testimonial/status/<int:id>/', views.statusTestimonial, name="testimonial.status"),
    path('testimonial/delete/<int:id>/', views.deleteTestimonial, name="testimonial.delete"),
]
