from django.db import models

from DjangoBaseSetup.common_modules.models import CommonModels


# Create your models here.
class Service(CommonModels):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='service_images/', blank=True, null=True)
    icon = models.ImageField(upload_to='service_icons/', blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_delete = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'service'

    def __str__(self):
        return self.name
