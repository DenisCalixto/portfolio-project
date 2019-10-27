from rest_framework import serializers

from .models import (
    Property,
    Inspection,
    InspectionFile,
    InspectionTemplate,
    InspectionTemplateSection,
    InspectionTemplateItem,
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
            "address",
            "thumbnail",
        )


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = (
            "id",
            "name",
            "notes",
            "address",
            "unit",
            "zipcode",
            "city",
            "province",
            "property_type",
            "thumbnail",
            "owner",
            "contact",
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


class InspectionTemplateItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionTemplateItem
        fields = (
            "id",
            "name",
        )


class InspectionTemplateSectionSerializer(serializers.ModelSerializer):
    items = InspectionTemplateItemSerializer(many=True, read_only=True)
    class Meta:
        model = InspectionTemplateSection
        fields = (
            "id",
            "name",
            "items",
        )


class InspectionTemplateSerializer(serializers.ModelSerializer):
    sections = InspectionTemplateSectionSerializer(many=True, read_only=True)
    class Meta:
        model = InspectionTemplate
        fields = (
            "id",
            "name",
            "property_type",
            "sections",
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
