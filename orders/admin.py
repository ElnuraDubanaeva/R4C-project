from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "robot_serial", "created_at")
    list_filter = (
        "customer",
        "robot_serial",
    )
    search_fields = ("robot_serial",)
    ordering = ("-created_at",)
    fields = ("customer", "robot_serial", "created_at", "is_deleted")
    readonly_fields = ("created_at",)
    list_per_page = 25
