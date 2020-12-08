from django.db import models
from core import models as core_models
from django.utils.translation import gettext_lazy as _


class Reservation(core_models.AbstractTimeStampModel):

    """ Reservation Model Definition """

    class ReservationStatus(models.TextChoices):
        confirmed = "CONFIRMED", _("Confirmed")
        pending = "PENDING", _("Pending")
        canceled = "CANCELED", _("Canceled")

    room = models.ForeignKey(
        "rooms.Room", related_name="reservations", on_delete=models.CASCADE, null=False
    )
    guest = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE, null=False
    )
    check_in_time = models.DateField()
    check_out_time = models.DateField()
    reservation_status = models.CharField(
        max_length=10,
        choices=ReservationStatus.choices,
        null=False,
        default=ReservationStatus.pending,
    )

    def __str__(self):
        return f"{self.room} - {self.check_in_time}"
