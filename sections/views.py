from django.shortcuts import redirect,render
from sections.models import Skill,Story
from django.contrib.auth.decorators import login_required

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

@login_required
def add_stories(request):
    form = StoryForm
    return render(request, 'addstories.html',{ "form" :form})

@login_required
def add_skills(request):
    form = SkillForm
    if request.method == "POST":
        if form.is_valid:
            name = request.POST.get('name')
            description = request.POST.get('description')
            skill_obj = Skill(name = name, description = description)
            skill_obj.save()
            return redirect('/')
    return render(request, 'addskills.html',{ "form" :form})