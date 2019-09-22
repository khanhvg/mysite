from django.shortcuts import render
from first_app.models import Topic, Webpage, Content, Category, Course


# Create your views here.

def webpage(request):
    return render(request, 'secondapp/webpage.html')


def topic(request):
    return render(request, 'secondapp/topic.html')
