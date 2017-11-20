"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from  django.views.generic.base import TemplateView
from util.mongoConnection import QuestionsCollection
import json
from bson.json_util import dumps
from django.core import serializers
from simple_rest import Resource
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page'
        }
    )

class QuestionListView(LoginRequiredMixin, TemplateView):
    template_name = "app/list.html"
    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        #questionsCollection = QuestionsCollection()
        #context['questions'] = dumps(questionsCollection.getQuestionList())
        #context['latest_articles'] = Article.objects.all()[:5]
        return context

class QuestionsAPI(LoginRequiredMixin, Resource):

    def get(self, request):
        queryParams = request.GET.dict()
        questions = QuestionsCollection().getQuestionList(queryParams)
        return HttpResponse(dumps(questions), content_type = 'application/json', status = 200)

    def post(self, request):
        # create.
        queryParams = request.POST.dict()
        questionsCollection = QuestionsCollection()
        id = questionsCollection.addQuestion(queryParams)
        newQuestion = questionsCollection.getQuestionById(id)
        return self.to_json(newQuestion)

    def put(self, request, id):
        queryParams = request.POST.dict()
        questionsCollection = QuestionsCollection()
        questionsCollection.updateQuestion(id, queryParams)
        updatedQuestion = questionsCollection.getQuestionById(id)
        return self.to_json(updatedQuestion)

    def delete(self, request, id):
        queryParams = request.POST.dict()
        QuestionsCollection().deleteQuestion(id)
        return HttpResponse(status = 200)

    def to_json(self, obj):
        return HttpResponse(dumps(obj), content_type = 'application/json', status = 200)