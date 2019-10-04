from .models import (
    Property,
    Inspection,
    InspectionFile,
    Report,
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
            "modified",
            "created",
        )

class InspectionFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionFile
        fields = (
            "id",
            "inspection",
            "picture",
            "notes",
            "modified",
            "created",
        )


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = (
            "id",
            "inspection",
            "signature",
            "notes",
            "status",
            "modified",
            "created",
        )
