from django import forms

from app.models import *

class TopicForm(forms.Form):
    Tname=forms.CharField()

 


class WebpageForm(forms.Form):
    tl=[[to.topic_name,to.topic_name] for to in topic.objects.all() ]
    topic_name=forms.ChoiceField(choices=tl)
    name=forms.CharField()
    url=forms.URLField()
    email=forms.EmailField()

 