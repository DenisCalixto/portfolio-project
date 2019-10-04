from django.db import models

from users.models import User

class BaseModel(models.Model):
    modified = models.DateTimeField("date modified", auto_now=True, blank=True)
    created = models.DateTimeField("date created", auto_now_add=True, blank=True)

    class Meta:
        abstract = True

class Property(BaseModel):
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


class Inspection(BaseModel):
    inspector = models.ForeignKey("users.User", null=True, on_delete=models.SET_NULL)
    inspected_property = models.ForeignKey(
        Property, null=True, default=None, on_delete=models.SET_NULL
    )
    inspection_date = models.DateTimeField("when the inspection occured", null=True, blank=True)
    notes = models.TextField(null=True, blank=True, default="")
    
    # Choices Constants:
    DRAFT = "DR"
    FINALIZED = "FI"
    # Choices:
    # first element: constant Python identifier
    # second element: human-readable version
    STATUS_CHOICES = [
        (DRAFT, "Draft"),
        (FINALIZED, "Finalized"),
    ]
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, null=True, default=DRAFT
    )


class InspectionFile(BaseModel):
    inspection = models.ForeignKey(
        Inspection, null=True, default=None, on_delete=models.SET_NULL, related_name="files"
    )
    picture = models.ImageField(upload_to='inspections_files/', null=True)
    notes = models.TextField(null=True, blank=True, default="")
