from django.db import models

from DjangoBaseSetup.common_modules.models import CommonModels


# Create your models here.
class Message(CommonModels):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    is_sent = models.BooleanField(default=False, blank=True, null=True)
    is_delete = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 'message'

    def __str__(self):
        return self.subject


class Testimonial(CommonModels):
    client_name = models.CharField(max_length=100, blank=True, null=True)
    client_image = models.ImageField(upload_to='testimonial_images/', blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_delete = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 'testimonial'

    def __str__(self):
        return self.client_name
