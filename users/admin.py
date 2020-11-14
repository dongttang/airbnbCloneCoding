from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin Definition """

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
