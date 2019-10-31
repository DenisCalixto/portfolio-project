from django.shortcuts import render
from django.db.models import Q
from django.core import serializers
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import (
    Property,
    Inspection,
    InspectionFile,
    InspectionTemplate,
    InspectionTemplateSection,
    InspectionTemplateItem,
    Report,
)
from .serializers import (
    PropertySerializer,
    InspectionSerializer,
    InspectionFileSerializer,
    InspectionTemplateSerializer,
    ReportSerializer,
)


class PropertyViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()


class InspectionViewSet(viewsets.ModelViewSet):
    serializer_class = InspectionSerializer
    queryset = Inspection.objects.all()

    @method_decorator(never_cache)
    @action(detail=False)
    def get_draft_by_property(self, request):
        properties = Inspection.objects.filter(Q(inspected_property__id__exact=request.GET.get("property_id"))) \
                    .values('id', 'inspector', 'inspection_date', 'status')
        properties_list = list(properties)  # important: convert the QuerySet to a list object
        if len(properties_list) > 0:
            return JsonResponse(properties_list[0], safe=False)
        else:
            return JsonResponse({}, safe=False)


class InspectionTemplateViewSet(viewsets.ModelViewSet):
    serializer_class = InspectionTemplateSerializer
    queryset = InspectionTemplate.objects.all()


class InspectionFileViewSet(viewsets.ModelViewSet):
    serializer_class = InspectionFileSerializer
    queryset = InspectionFile.objects.all()


class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()

