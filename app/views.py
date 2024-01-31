from django.shortcuts import render
from app.models import *

# Create your views here.
from app.forms import *
from django.http import HttpResponse


def insert_topic(request):
     ETFO=TopicForm()
     d={'ETFO':ETFO}

     if request.method=='POST':
        ETFO=TopicForm(request.POST)
        if ETFO.is_valid():
             tn=request.POST['Tname']

             TO=topic.objects.get_or_create(topic_name=tn)[0]
             TO.save() 

             return HttpResponse( 'Create successfully')

     return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}

    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            TO=topic.objects.get(topic_name=tn)
            n=WFDO.cleaned_data['name']
            u=WFDO.cleaned_data['url']
            e=WFDO.cleaned_data['email']
            WO=webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
            WO.save()

            return HttpResponse( 'Create successfully') 
    return render(request,'insert_webpage.html',d)


