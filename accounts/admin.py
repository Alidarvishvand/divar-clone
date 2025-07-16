from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, Profile
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm   # ← این دو خط مهم هستند
    form = CustomUserChangeForm         # ←

    ordering = ["email"]
    list_display = ["id", "email", "phone", "first_name", "is_staff", "is_active"]
    search_fields = ["email", "phone", "first_name", "last_name"]
    readonly_fields = ["created_date", "updated_date"]

    fieldsets = (
        (None, {"fields": ("email", "phone", "password")}),
        (_("Personal Info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_verified",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            _("Important dates"),
            {"fields": ("last_login", "created_date", "updated_date")},
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "phone",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                ),
            },
        ),
    )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "location"]
    search_fields = ["user__email", "user__phone"]
