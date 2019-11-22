from rest_framework import serializers

from .models import (
    Property,
    Inspection,
    InspectionSection,
    InspectionItem,
    InspectionFile,
    InspectionTemplate,
    InspectionTemplateSection,
    InspectionTemplateItem,
    Report,
)

from users.models import (
    User
)
from users.serializers import UserSerializer


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


class InspectionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionItem
        fields = (
            "id",
            "name",
            "inspection_section",
            "notes",
            "picture",
            "status",
            "modified",
            "created",
        )


class InspectionSectionSerializer(serializers.ModelSerializer):
    items = InspectionItemSerializer(many=True, read_only=True)
    class Meta:
        model = InspectionSection
        fields = (
            "id",
            "name",
            "inspection",
            "items",
            "modified",
            "created",
        )


class InspectionSerializer(serializers.ModelSerializer):
    sections = InspectionSectionSerializer(many=True, read_only=True)
    inspected_property_obj = PropertyLightSerializer(source="inspected_property", read_only=True)
    class Meta:
        model = Inspection
        fields = (
            "id",
            "inspector",
            "inspected_property",
            "inspected_property_obj",
            "inspection_date",
            "sections",
            "notes",
            "tenant_name",
            "tenant_phone",
            "tenant_email",
            "tenant_notes",
            "status",
            "modified",
            "created",
        )


class InspectionDetailSerializer(serializers.ModelSerializer):
    inspector = UserLightSerializer(read_only=True)
    inspected_property = PropertyLightSerializer(read_only=True)
    sections = InspectionSectionSerializer(many=True, read_only=True)
    class Meta:
        model = Inspection
        fields = (
            "id",
            "inspector",
            "inspected_property",
            "inspection_date",
            "sections",
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
            "tenant_name",
        )


class InspectionTemplateItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionTemplateItem
        fields = (
            "id",
            "name",
        )


class InspectionTemplateSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionTemplateSection
        fields = (
            "id",
            "name",
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
    inspection_obj = InspectionLightSerializer(source="inspection", read_only=True)
    class Meta:
        model = Report
        fields = (
            "id",
            "inspection",
            "inspection_obj",
            "signature",
            "report_file",
            "notes",
            "status",
            "modified",
            "created",
        )
