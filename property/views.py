from django.shortcuts import render
from rest_framework import viewsets

from .models import (
    Property,
    Inspection,
)
from .serializers import (
    PropertySerializer,
    InspectionSerializer,
)


class PropertyViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()


class InspectionViewSet(viewsets.ModelViewSet):
    serializer_class = InspectionSerializer
    queryset = Inspection.objects.all()
