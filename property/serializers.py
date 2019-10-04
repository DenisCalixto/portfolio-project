from .models import (
    Property,
    Inspection,
)
from rest_framework import serializers

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = (
            "id",
            "name",
            "description",
            "address",
            "city",
            "province",
            "property_type",
            "modified",
            "created",
        )

class InspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspection
        fields = (
            "id",
            "inspector",
            "inspected_property",
            "inspection_date",
            "notes",
            "status",
        )
