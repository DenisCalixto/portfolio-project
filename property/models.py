from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(null=True, blank=True, default="")

    address = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=64, default="", blank=True)
    province = models.CharField(max_length=32, default="", blank=True)

    # Choices Constants:
    PLACE = "PL"
    CAR = "CA"
    EQUIPMENT = "EQ"
    # Choices:
    # first element: constant Python identifier
    # second element: human-readable version
    PROPERTY_TYPE_CHOICES = [
        (PLACE, "Place"),
        (CAR, "Car"),
        (EQUIPMENT, "Equipment"),
    ]
    property_type = models.CharField(max_length=2, choices=PROPERTY_TYPE_CHOICES, blank=True, null=True)

    