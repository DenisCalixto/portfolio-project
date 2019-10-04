from .models import (
    Property,
    Inspection,
    InspectionFile,
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

class InspectionFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionFile
        fields = (
            "id",
            "inspection",
            "picture",
            "notes",
        )
