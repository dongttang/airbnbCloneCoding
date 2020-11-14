from django.db import models
from django.utils.translation import gettext_lazy as _
from core import models as core_models


class Review(core_models.AbstractTimeStampModel):

    list_filter = ["reviewed_room"]

    class Score(models.IntegerChoices):
        ONE = 1, _("⭐")
        TWO = 2, _("⭐⭐")
        THREE = 3, _("⭐⭐⭐")
        FOUR = 4, _("⭐⭐⭐⭐")
        FIVE = 5, _("⭐⭐⭐⭐⭐")

    review_context = models.TextField(null=False)
    cleanliness = models.IntegerField(choices=Score.choices, null=False)
    communication = models.IntegerField(choices=Score.choices, null=False)
    check_in = models.IntegerField(choices=Score.choices, null=False)
    accuracy = models.IntegerField(choices=Score.choices, null=False)
    location = models.IntegerField(choices=Score.choices, null=False)
    value = models.IntegerField(choices=Score.choices, null=False)
    reviewed_room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )
    reviewer = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.reviewed_room
