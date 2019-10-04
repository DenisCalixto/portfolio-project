from .models import (
    Property,
)
from rest_framework import serializers

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = (
            "name",
            "description",
            "address",
            "city",
            "province",
            "property_type",
            "modified",
            "created",
        )
