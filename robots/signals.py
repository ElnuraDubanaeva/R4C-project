from django.db.models.signals import post_save
from django.dispatch import receiver
from orders.models import Order
from customers.services import CustomerEmailService
from .models import Robot


@receiver(post_save, sender=Robot)
def check_robot_availability(sender, instance, **kwargs):
    orders = Order.objects.filter(robot_serial=instance.serial).distinct()
    if orders.exists():
        recipient_list = list(orders.values_list("customer__email", flat=True))
        CustomerEmailService.send_email(robot=instance, recipient_list=recipient_list)
