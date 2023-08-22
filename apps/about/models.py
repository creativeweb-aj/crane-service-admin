from django.db import models
from DjangoBaseSetup.common_modules.models import CommonModels


# Create your models here.
class About(CommonModels):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_delete = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 'about'

    def __str__(self):
        return self.title


class KeyPoint(CommonModels):
    icon = models.ImageField(upload_to='keypoint_icons/', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_delete = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 'key_point'

    def __str__(self):
        return self.name


class OurValue(CommonModels):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_delete = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 'our_value'

    def __str__(self):
        return self.title


class Person(CommonModels):
    name = models.CharField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='person_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_delete = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 'person'

    def __str__(self):
        return self.name


class WorkingDay(CommonModels):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    day = models.CharField(max_length=10, choices=DAY_CHOICES, blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_delete = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 'working_days'

    def __str__(self):
        return f"{self.get_day_display()} - {self.start_time.strftime('%I:%M %p')} to {self.end_time.strftime('%I:%M %p')}"
