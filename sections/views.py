from django.http import HttpResponse
from django.shortcuts import render
from sections.models import Skill,Story

from django import forms
from .models import Story


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields  = ['title','category','content']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 100, 'rows': 30}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields  = ['name','description']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 100, 'rows': 30}),
        }

def main(request):
    skills = Skill.objects.all()
    stories = Story.objects.all()
    return render(request,'main.html',
    {'skills': skills,
     'stories': stories})

def skills(request):
    skills = Skill.objects.all()
    return render(request,'skill.html',
    {'skills': skills})

def add_stories(request):
    form = StoryForm
    return render(request, 'stories.html',{ "form" :form})

def add_skills(request):
    form = StoryForm
    return render(request, 'skills.html',{ "form" :form})