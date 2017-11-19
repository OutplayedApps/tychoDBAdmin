"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from  django.views.generic.base import TemplateView
from util.mongoConnection import QuestionsCollection
import json
from bson.json_util import dumps

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

class QuestionListView(TemplateView):
    template_name = "app/list.html"
    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        questionsCollection = QuestionsCollection()
        context['questions'] = dumps(questionsCollection.getQuestionList())
        #context['latest_articles'] = Article.objects.all()[:5]
        return context