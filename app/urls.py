"""
Definition of urls for djangoapp.
"""

from datetime import datetime
from django.conf.urls import url, include

from .views import QuestionListView, QuestionsAPI
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Examples:
    url(r'^list/', QuestionListView.as_view(), name='list'),
    url(r'^api/?$', QuestionsAPI.as_view()),
    url(r'^api/(?P<id>[a-z0-9]+)?$', QuestionsAPI.as_view()),
    url(r'^$', auth_views.LoginView.as_view(), name='home'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url('^accounts/', include('django.contrib.auth.urls')),
]
