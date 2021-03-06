from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'property', views.PropertyViewSet)
router.register(r'inspection', views.InspectionViewSet)
router.register(r'inspection_section', views.InspectionSectionViewSet)
router.register(r'inspection_item', views.InspectionItemViewSet)
router.register(r'inspectionfile', views.InspectionFileViewSet)
router.register(r'inspection_template', views.InspectionTemplateViewSet)
router.register(r'inspection_template_item', views.InspectionTemplateItemViewSet)
router.register(r'report', views.ReportViewSet)

urlpatterns = [
    path('', include(router.urls))
]
