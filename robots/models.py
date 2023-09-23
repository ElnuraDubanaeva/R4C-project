from django.db import models
from common.models import BaseModel


class Robot(BaseModel):
    serial = models.CharField(
        max_length=5, blank=False, null=False, verbose_name="Серийный номер"
    )
    model = models.CharField(
        max_length=2, blank=False, null=False, verbose_name="Модель"
    )
    version = models.CharField(
        max_length=2, blank=False, null=False, verbose_name="Версия"
    )

    def __str__(self) -> str:
        return self.serial

    class Meta:
        verbose_name = "Robot"
        verbose_name_plural = "Robots"
        ordering = ("-created_at",)
