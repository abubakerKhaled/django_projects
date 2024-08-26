from django.http import HttpResponse
#from django.template import loader
#from django.http import Http404

# this is the shortcuts of the HttpResponse and loader moduls
# this is the shortcuts of the Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Question

app_name = "polls"

def index(request):
    latest_questions = get_list_or_404(Question)[:5]
    context = {
            'latest_questions': latest_questions,
        }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)