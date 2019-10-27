from django.contrib import admin

from .models import (
    Property,
    Inspection,
    InspectionFile,
    InspectionTemplate,
    InspectionTemplateSection,
    InspectionTemplateItem,
    Report,
)

admin.site.register(Property)
admin.site.register(Inspection)
admin.site.register(InspectionFile)
admin.site.register(InspectionTemplate)
admin.site.register(InspectionTemplateSection)
admin.site.register(InspectionTemplateItem)
admin.site.register(Report)
