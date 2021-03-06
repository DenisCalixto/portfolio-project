from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
from property.views import report_pdf

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
    url('api-auth/', include('rest_framework.urls')),
    url('api/token/', TokenObtainPairView.as_view()),
    url('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/', include('jobs.urls')),
    path("api/", include("users.urls"), name="users"),
    path("api/", include("property.urls"), name="property"),
    path('report_pdf/<int:report_id>/', report_pdf, name='report_pdf'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
