from rest_framework import serializers

from .models import (
    Property,
    Inspection,
    InspectionFile,
    Report,
)

from users.models import (
    User
)

class UserLightSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
        )

class PropertyLightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = (
            "id",
            "name",
            "thumbnail",
        )

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
            "thumbnail",
            "modified",
            "created",
        )

class InspectionSerializer(serializers.ModelSerializer):
    inspector = UserLightSerializer()
    inspected_property = PropertyLightSerializer()
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

class InspectionLightSerializer(serializers.ModelSerializer):
    inspected_property = PropertyLightSerializer()
    class Meta:
        model = Inspection
        fields = (
            "id",
            "inspected_property",
            "inspection_date",
        )

class ReportSerializer(serializers.ModelSerializer):
    inspection = InspectionLightSerializer()
    class Meta:
        model = Report
        fields = (
            "id",
            "inspection",
            "signature",
            "report_file",
            "notes",
            "status",
            "modified",
            "created",
        )
