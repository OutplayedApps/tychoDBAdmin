"""
Definition of urls for djangoapp.
"""

from datetime import datetime
from django.conf.urls import url

import app.forms
import app.views
from .views import QuestionListView


urlpatterns = [
    # Examples:
    url(r'^list/', QuestionListView.as_view(), name='list'),
    url(r'^$', app.views.home, name='home')
]
