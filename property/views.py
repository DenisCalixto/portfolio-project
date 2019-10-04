from django.shortcuts import render
from rest_framework import viewsets

from .models import (
    Property,
    Inspection,
    InspectionFile,
)
from .serializers import (
    PropertySerializer,
    InspectionSerializer,
    InspectionFileSerializer,
)


class PropertyViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()


class InspectionViewSet(viewsets.ModelViewSet):
    serializer_class = InspectionSerializer
    queryset = Inspection.objects.all()


class InspectionFileViewSet(viewsets.ModelViewSet):
    serializer_class = InspectionFileSerializer
    queryset = InspectionFile.objects.all()
