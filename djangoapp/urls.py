"""
Definition of urls for djangoapp.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('app.urls'))
]
