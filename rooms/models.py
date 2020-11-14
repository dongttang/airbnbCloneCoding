from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

# Create your models here.


class AbstractItem(core_models.AbstractTimeStampModel):

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):
    class Meta:
        verbose_name = "Amenity"
        verbose_name_plural = "Amenities"


class Room(core_models.AbstractTimeStampModel):

    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
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

    def __str__(self):
        return self.room_title
