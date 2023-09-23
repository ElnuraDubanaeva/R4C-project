from django.db import models
from uuid import uuid4


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        unique=True,
        verbose_name=("ID"),
    )
    is_deleted = models.BooleanField(default=False, verbose_name=("удаленный?"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=("дата создания"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=("дата изменения"))

    class Meta:
        abstract = True
