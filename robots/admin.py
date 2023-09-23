from django.contrib import admin
from .models import Robot


@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    list_display = ("serial", "model", "version", "created")
    list_filter = ("model", "version")
    search_fields = ("serial", "model", "version")
    ordering = ("-created", "created_at")
    fields = ("serial", "model", "version", "created", "created_at", "is_deleted")
    readonly_fields = ("created_at", "created")
    list_per_page = 25
