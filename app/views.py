from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from app.models import *

# Create your views here.

def insert_topic(request):
    TFEO=TopicForm()
    d={'TFEO':TFEO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            topic_name=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
            TO.save()
            
            QLTO=Topic.objects.all()
            d1={'QLTO':QLTO}
            return render(request,'display_topic.html',d1)
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WFEO=WebpageForm()
    d={'WFEO':WFEO}
    if request.method=="POST":
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            topic_name=WFDO.cleaned_data['topic_name']
            name=WFDO.cleaned_data['name']
            url=WFDO.cleaned_data['url']
            TO=Topic.objects.get(topic_name=topic_name)

            QWO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
            QWO.save()
            
            QLWO=Webpage.objects.all()
            d1={'QLWO':QLWO}
            return render(request,'display_webpage.html',d1)
        
    return render(request,'insert_webpage.html',d)


def insert_access(request):
    AFEO=AccessrecordForm()
    d={'AFEO':AFEO}
    if request.method=='POST':
        ATDO=AccessrecordForm(request.POST)
        if ATDO.is_valid():
            name=ATDO.cleaned_data['name']
            author=ATDO.cleaned_data['author']
            date=ATDO.cleaned_data['date']
            WO=Webpage.objects.get(name=name)

            QAO=Accessrecord.objects.get_or_create(name=WO,author=author,date=date)[0]
            QAO.save()

            QLAO=Accessrecord.objects.all()
            d1={'QLAO':QLAO}
            return render(request,'display_access.html',d1)

    return render(request,'insert_access.html',d)
