from django.db import models

from DjangoBaseSetup.common_modules.models import CommonModels
from apps.users.models import User


# Create your models here.
class Staff(CommonModels):
    STAFF_TYPE_CHOICES = [
        ('driver', 'Driver'),
        ('helper', 'Helper'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    staff_type = models.CharField(max_length=6, choices=STAFF_TYPE_CHOICES, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'staff'

    def __str__(self):
        return self.user


class Customer(CommonModels):
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_email = models.EmailField(blank=True, null=True)
    customer_mobile = models.CharField(max_length=15, blank=True, null=True)
    customer_address = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return self.customer_name
