from django.db import models
from common.models import BaseModel


class Customer(BaseModel):
    email = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Емайл"
    )

    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = ("-created_at",)
