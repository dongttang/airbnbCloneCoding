from django.contrib import admin
from . import models as lists_models


@admin.register(lists_models.List)
class ListAdmin(admin.ModelAdmin):

    """ List Admin Definition """

    pass
