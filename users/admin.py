from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            (
                "Custom profile",
                {
                    "fields": (
                        "avata",
                        "gender",
                        "bio",
                        "birthday",
                        "language",
                        "currency",
                        "superhost",
                    )
                },
            )
        ),
    )
