from django.db import models
from common.models import BaseModel


class Robot(BaseModel):
    serial = models.CharField(
        max_length=5,
        blank=False,
        null=False,
        unique=True,
        verbose_name="Серийный номер",
    )
    model = models.CharField(
        max_length=2, blank=False, null=False, verbose_name="Модель"
    )
    version = models.CharField(
        max_length=2, blank=False, null=False, verbose_name="Версия"
    )
    created = models.DateTimeField(
        blank=False, null=False, verbose_name="Дата создание Робота"
    )

    def __str__(self) -> str:
        return str(self.serial)

    class Meta:
        verbose_name = "Robot"
        verbose_name_plural = "Robots"
        ordering = ("-created",)
