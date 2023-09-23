from django.db import models

from customers.models import Customer
from common.models import BaseModel


class Order(BaseModel):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="customer",
    )
    robot_serial = models.CharField(
        max_length=5, blank=False, null=False, verbose_name="Серийный номер"
    )

    def __str__(self) -> str:
        return self.robot_serial

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ("-created_at",)
