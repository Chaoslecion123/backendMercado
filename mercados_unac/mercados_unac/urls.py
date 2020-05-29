"""Main URLs module."""

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('apps.users.urls','users'),namespace='users'))
]
