from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Membership", {"fields": ("is_premium",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Membership", {"fields": ("is_premium",)}),
    )
    list_display = ("username", "email", "is_premium", "is_staff")
