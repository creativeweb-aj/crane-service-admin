from django.db import models
from DjangoBaseSetup.common_modules.models import CommonModels


# Create your models here.
class Crane(CommonModels):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_delete = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 'crane'

    def __str__(self):
        return self.name


class Project(CommonModels):
    crane = models.ForeignKey(Crane, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_delete = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 'project'

    def __str__(self):
        return self.title
