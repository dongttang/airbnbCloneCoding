from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = "M", _("male")
        FEMALE = "F", _("female")
        OTHER = "O", _("other")

    class Language(models.TextChoices):
        LANGUAGE_ENGLISH = "EN", _("English")
        LANGUAGE_KOREAN = "KO", _("한국어")
        LANGUAGE_JAPANESE = "JP", _("日本語")

    class Currency(models.TextChoices):
        USD = "USD", _("USD")
        KRW = "KRW", _("KRW")
        JPY = "JPY", _("JPY")

    avata = models.ImageField(blank=True)
    gender = models.CharField(max_length=1, choices=Gender.choices, blank=True)
    bio = models.TextField(blank=True)
    birthday = models.DateField(blank=True, null=True)
    language = models.CharField(max_length=2, choices=Language.choices, blank=True)
    currency = models.CharField(max_length=3, choices=Currency.choices, blank=True)
    superhost = models.BooleanField(default=False)
