from django.contrib import admin
from . import models as rooms_models

# Register your models here.


@admin.register(
    rooms_models.RoomType,
    rooms_models.Amenity,
    rooms_models.Facility,
    rooms_models.HouseRule,
)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(rooms_models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """
    
    pass


@admin.register(rooms_models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass
