import os
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core import serializers
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.http import JsonResponse

from django.core.files import File

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

import pdfkit

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
from users.models import User

from .serializers import (
    PropertySerializer,
    InspectionSerializer,
    InspectionSectionSerializer,
    InspectionItemSerializer,
    InspectionFileSerializer,
    InspectionTemplateSerializer,
    InspectionTemplateItemSerializer,
    ReportSerializer,
)


class PropertyViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()

    def filter_queryset(self, queryset):
        queryset = super(PropertyViewSet, self).filter_queryset(queryset)
        return queryset.order_by('-modified')


class InspectionViewSet(viewsets.ModelViewSet):
    serializer_class = InspectionSerializer
    queryset = Inspection.objects.all()

    def filter_queryset(self, queryset):
        queryset = super(InspectionViewSet, self).filter_queryset(queryset)
        return queryset.order_by('-modified')

    @method_decorator(never_cache)
    @action(detail=False)
    def get_draft_by_property(self, request):
        inspections = Inspection.objects.filter(Q(inspected_property__id__exact=request.GET.get("property_id")))
        inspections_list = list(inspections)  # important: convert the QuerySet to a list object
        if len(inspections_list) > 0:
            serializer = InspectionSerializer(inspections_list[0])
            return Response(serializer.data)
            # return JsonResponse(inspections_list[0], safe=False)
        else:
            return JsonResponse({}, safe=False)

    @method_decorator(never_cache)
    @action(detail=False, methods=["post"])
    def create_draft(self, request):
        print(request.data)
        propertyInspected = Property.objects.get(pk=int(request.data["property_id"]))

        inspection = Inspection()
        inspection.inspected_property = propertyInspected
        inspection.status = Inspection.DRAFT
        if 'user_id' in request.data.keys():
            user = User.objects.get(pk=int(request.data["user_id"]))
            inspection.inspector = user
        inspection.save()

        # Add sections
        template_sections = InspectionTemplateSection.objects.all()
        template_items = InspectionTemplateItem.objects.all()
        for template_section in template_sections:
            section = InspectionSection.objects.create(
                inspection = inspection,
                name = template_section.name,
            )
            # for template_item in template_items:
            #     item = InspectionItem.objects.create(
            #         inspection_section = section,
            #         name = template_item.name,
            #     )

        serializer = InspectionSerializer(inspection)
        return Response(serializer.data)


class InspectionSectionViewSet(viewsets.ModelViewSet):
    serializer_class = InspectionSectionSerializer
    queryset = InspectionSection.objects.all()


class InspectionItemViewSet(viewsets.ModelViewSet):
    serializer_class = InspectionItemSerializer
    queryset = InspectionItem.objects.all()


class InspectionTemplateItemViewSet(viewsets.ModelViewSet):
    serializer_class = InspectionTemplateItemSerializer
    queryset = InspectionTemplateItem.objects.all()


class InspectionTemplateViewSet(viewsets.ModelViewSet):
    serializer_class = InspectionTemplateSerializer
    queryset = InspectionTemplate.objects.all()


class InspectionFileViewSet(viewsets.ModelViewSet):
    serializer_class = InspectionFileSerializer
    queryset = InspectionFile.objects.all()


class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()

    def filter_queryset(self, queryset):
        queryset = super(ReportViewSet, self).filter_queryset(queryset)
        return queryset.order_by('-modified')

    @method_decorator(never_cache)
    @action(detail=False, methods=["get"])
    def create_report_file(self, request):

        # report_id = request.GET.get("report_id")
        # pdfkit.from_url('https://greenfillproject.com/report_pdf/{}/'.format(str(report_id)), 'micro.pdf')
        pdfkit.from_url('https://greenfillproject.com/report_pdf?report_id=14', 'micro.pdf')
        # report = get_object_or_404(Report, pk=report_id)

        # pdfkit.from_url('https://greenfillproject.com/', 'micro.pdf')

        # f = open('micro.pdf')
        # report.save(new_name, File(f))

        return Response([])

def report_pdf(request, report_id):    
    inspection = get_object_or_404(Inspection, pk=report_id)
    inspected_property = inspection.inspected_property
    reports = Report.objects.filter(inspection__id=inspection.id)
    reports_list = list(reports)
    sections = inspection.sections
    return render(
        request,
        'report_pdf.html', 
        { 
            'inspection': inspection,
            'inspected_property': inspected_property,
            'report': reports_list[0],
            'sections': sections,
        }
    )
