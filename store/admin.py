from django.contrib import admin

from .models import ContactMessage, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "is_featured", "created_at")
    list_filter = ("is_featured",)
    search_fields = ("title", "description")
    list_editable = ("is_featured",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    readonly_fields = ("created_at",)