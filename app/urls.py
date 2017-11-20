"""
Definition of urls for djangoapp.
"""

from datetime import datetime
from django.conf.urls import url

import app.forms
import app.views
from .views import QuestionListView, QuestionsAPI


urlpatterns = [
    # Examples:
    url(r'^list/', QuestionListView.as_view(), name='list'),
    url(r'^api/?$', QuestionsAPI.as_view()),
    url(r'^api/(?P<id>[a-z0-9]+)?$', QuestionsAPI.as_view()),
    url(r'^$', app.views.home, name='home')
]
