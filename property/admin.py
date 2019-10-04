from django.contrib import admin

from .models import (
    Property,
    Inspection,
)

admin.site.register(Property)
admin.site.register(Inspection)
