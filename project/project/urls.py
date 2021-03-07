"""

    project URL Configuration

"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += [
     path('CRM/', include('CRM.urls')),
     path('', RedirectView.as_view(url='/CRM/', permanent=True)),
     path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
