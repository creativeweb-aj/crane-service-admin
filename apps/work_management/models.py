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
        return f"{self.user.first_name} {self.user.last_name}".strip()


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


class Work(CommonModels):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    work_title = models.CharField(max_length=100, blank=True, null=True)
    work_detail = models.TextField(blank=True, null=True)
    work_location = models.CharField(max_length=100, blank=True, null=True)
    start_date_time = models.DateTimeField(blank=True, null=True)
    end_date_time = models.DateTimeField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pending_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    drivers = models.ManyToManyField('Staff', related_name='work_as_driver', blank=True,
                                     limit_choices_to={'staff_type': 'driver'})
    helpers = models.ManyToManyField('Staff', related_name='work_as_helper', blank=True,
                                     limit_choices_to={'staff_type': 'helper'})

    class Meta:
        db_table = 'work'

    def __str__(self):
        return self.work_title

