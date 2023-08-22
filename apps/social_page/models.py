from django.db import models
from DjangoBaseSetup.common_modules.models import CommonModels


# Create your models here.
class SocialPage(CommonModels):
    name = models.CharField(max_length=100, blank=True, null=True)
    icon = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_delete = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 'social_page'

    def __str__(self):
        return self.name


class SocialLink(CommonModels):
    social_page = models.ForeignKey(SocialPage, on_delete=models.CASCADE, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_delete = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 'social_link'

    def __str__(self):
        return f"Social Link for {self.social_page.name}"
