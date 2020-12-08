from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.AbstractTimeStampModel):

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Photo(core_models.AbstractTimeStampModel):

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", related_name="photo", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class RoomType(AbstractItem):
    class Meta:
        verbose_name = "Room Type"
        ordering = ["name"]


class Amenity(AbstractItem):
    class Meta:
        verbose_name = "Amenity"
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    class Meta:
        verbose_name = "Facility"
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    class Meta:
        verbose_name = "House Rule"
        verbose_name_plural = "House Rules"


class Room(core_models.AbstractTimeStampModel):

    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_title = models.CharField(max_length=80)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=80)
    latitude = models.DecimalField(decimal_places=6, max_digits=6)
    longitude = models.DecimalField(decimal_places=6, max_digits=6)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.room_title
