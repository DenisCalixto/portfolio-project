from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('api/', include('jobs.urls')),
    path("api/", include("users.urls"), name="users"),
    path("api/", include("property.urls"), name="property"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
