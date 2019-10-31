from django.db import models

from users.models import User


class BaseModel(models.Model):
    modified = models.DateTimeField("date modified", auto_now=True, blank=True)
    created = models.DateTimeField("date created", auto_now_add=True, blank=True)

    class Meta:
        abstract = True


class Property(BaseModel):
    name = models.CharField(max_length=64, blank=True, null=True)
    notes = models.TextField(null=True, blank=True, default="")

    address = models.CharField(max_length=128, blank=True, null=True)
    unit = models.CharField(max_length=16, default="", blank=True)
    zipcode = models.CharField(max_length=16, default="", blank=True)
    city = models.CharField(max_length=64, default="", blank=True)
    province = models.CharField(max_length=32, default="", blank=True)
    owner = models.CharField(max_length=64, default="", blank=True)
    contact = models.CharField(max_length=32, default="", blank=True)
    
    thumbnail = models.ImageField(upload_to='properties_images/', null=True)

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
    
    def __str__(self):
        return self.address


class Inspection(BaseModel):
    inspector = models.ForeignKey("users.User", null=True, on_delete=models.SET_NULL)
    inspected_property = models.ForeignKey(
        Property, null=True, default=None, on_delete=models.SET_NULL
    )
    inspection_date = models.DateField("when the inspection occured", null=True, blank=True, auto_now_add=True)
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
    
    def __str__(self):
        if self.inspector:
            return str(self.inspection_date) + " - " + self.inspector.first_name + " " + self.inspector.last_name
        else:
            return str(self.inspection_date)


class InspectionSection(BaseModel):
    name = models.CharField(max_length=64, blank=True, null=True)
    inspection = models.ForeignKey(
        Inspection, null=True, default=None, on_delete=models.SET_NULL, related_name="sections"
    )

    def __str__(self):
        return self.name


class InspectionItem(BaseModel):
    name = models.CharField(max_length=64, blank=True, null=True)
    inspection_section = models.ForeignKey(
        InspectionSection, null=True, default=None, on_delete=models.SET_NULL, related_name="items"
    )
    notes = models.TextField(null=True, blank=True, default="")
    status = models.CharField(max_length=16, blank=True, null=True)
    
    def __str__(self):
        return self.name


class InspectionFile(BaseModel):
    inspection = models.ForeignKey(
        Inspection, null=True, default=None, on_delete=models.SET_NULL, related_name="inspection_files"
    )
    inspection_item = models.ForeignKey(
        InspectionItem, null=True, default=None, on_delete=models.SET_NULL, related_name="item_files"
    )
    picture = models.ImageField(upload_to='inspections_files/', null=True)


class InspectionTemplate(BaseModel):
    name = models.CharField(max_length=64, blank=True, null=True)

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
    
    def __str__(self):
        return self.name


class InspectionTemplateSection(BaseModel):
    name = models.CharField(max_length=64, blank=True, null=True)
    inspection_template = models.ForeignKey(
        InspectionTemplate, null=True, default=None, on_delete=models.SET_NULL, related_name="sections"
    )

    def __str__(self):
        return self.name


class InspectionTemplateItem(BaseModel):
    name = models.CharField(max_length=64, blank=True, null=True)
    inspection_section = models.ForeignKey(
        InspectionTemplateSection, null=True, default=None, on_delete=models.SET_NULL, related_name="items"
    )
    
    def __str__(self):
        return self.name


class Report(BaseModel):
    inspection = models.ForeignKey(
        Inspection, null=True, default=None, on_delete=models.SET_NULL, related_name="reports"
    )
    signature = models.ImageField(upload_to='report_signatures/', null=True)
    report_file = models.FileField(upload_to='reports/', null=True)
    notes = models.TextField(null=True, blank=True, default="")
    
    # Choices Constants:
    DRAFT = "DR"
    SIGNED = "SI"
    FINALIZED = "FI"
    # Choices:
    # first element: constant Python identifier
    # second element: human-readable version
    STATUS_CHOICES = [
        (DRAFT, "Draft"),
        (SIGNED, "Signed"),
        (FINALIZED, "Finalized"),
    ]
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, null=True, default=DRAFT
    )
    
    def __str__(self):
        return str(self.inspection.inspection_date) + " - " + self.inspection.inspector.first_name + " " + self.inspection.inspector.last_name
