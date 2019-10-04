from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'property', views.PropertyViewSet)
router.register(r'inspection', views.InspectionViewSet)

urlpatterns = [
    path('', include(router.urls))
]
