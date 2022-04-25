from django.shortcuts import render
from.models import Topic

# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html')

def topics(request):
    topics =Topic.objects.all()

    context ={'topics': topics} #key for html value for views

    return render(request,'MainApp/topics.html',context)