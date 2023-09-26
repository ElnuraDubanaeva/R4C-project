from customers.models import Customer
from robots.models import Robot
from .models import Order


class OrderService:
    __order_model = Order
    __customer_model = Customer
    __robot_model = Robot

    @classmethod
    def make_order(cls, form_cleaned_data):
        customer = cls.__customer_model.objects.get_or_create(
            email=form_cleaned_data.get("email")
        )
        robot_serial = (
            f"{form_cleaned_data.get('model')}-{form_cleaned_data.get('version')}"
        )
        cls.__order_model.objects.create(
            customer=customer[0], robot_serial=robot_serial
        )
        robot = cls.__robot_model.objects.filter(serial=robot_serial)
        if robot.exists():
            data = f"Ваш заказ {robot.first().serial} в наличий!"
        else:
            data = "Как только робот будет в наличий мы вам напишем на почту!"
        return data
