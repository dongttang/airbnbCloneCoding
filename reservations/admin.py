from django.contrib import admin
from . import models as resetvations_models


@admin.register(resetvations_models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """ Reservation Admin Definition """

    pass
