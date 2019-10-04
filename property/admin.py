from django.contrib import admin

from .models import (
    Property,
    Inspection,
    InspectionFile,
)

admin.site.register(Property)
admin.site.register(Inspection)
admin.site.register(InspectionFile)
