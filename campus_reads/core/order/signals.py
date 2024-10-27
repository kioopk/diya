from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from students.models import CustomUser

@receiver(post_save, sender=CustomUser)
def create_order_for_new_user(sender, instance, created, **kwargs):
    if created:
        Order.objects.create(user=instance)