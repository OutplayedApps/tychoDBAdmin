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
        #questionsCollection = QuestionsCollection()
        #context['questions'] = dumps(questionsCollection.getQuestionList())
        #context['latest_articles'] = Article.objects.all()[:5]
        return context

class QuestionsAPI(Resource):

    def get(self, request):
        queryParams = request.GET.dict()
        questions = QuestionsCollection().getQuestionList(queryParams)
        return HttpResponse(dumps(questions), content_type = 'application/json', status = 200)

    def post(self, request):
        # create.
        return HttpResponse(status = 201)

    def put(self, request, client_id):
        # get and save.
        return HttpResponse(status = 200)

    def delete(self, request, client_id):
        # get and delete.
        return HttpResponse(status = 200)

    #def to_json(self, objects):
    #    return serializers.serialize('json', objects)