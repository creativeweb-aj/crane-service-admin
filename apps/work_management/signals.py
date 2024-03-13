from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Work


@receiver(pre_save, sender=Work)
def update_pending_amount(sender, instance, **kwargs):
    """
    Signal to set pending_amount equal to amount just before saving a Work instance.
    """
    if instance.amount is not None:  # Check to ensure amount is not None
        instance.pending_amount = instance.amount
