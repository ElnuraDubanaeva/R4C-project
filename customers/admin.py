from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at")
    list_filter = ("email",)
    search_fields = ("email",)
    ordering = ("-created_at",)
    fields = ("email", "created_at", "is_deleted")
    readonly_fields = ("created_at",)
    list_per_page = 25
