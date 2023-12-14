from django.shortcuts import redirect,render
from sections.models import Skill,Story
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django import forms
from .models import Story
from django.views.generic import ListView, CreateView  # new
from .utils import get_sublists

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields  = ['title','category','content','cover']
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

def mosaic(request):
    stories = Story.objects.all()
    s1,s2,s3,s4 = get_sublists(stories,4)
    return render(request,'mosaic.html',
    {'stories1': s1,
     'stories2': s2,
     'stories3': s3,
     'stories4': s4})

def story(request, id):
    story = Story.objects.get(id=id)
    return render(request, 'story.html', {'story' : story})

@method_decorator(login_required, name="dispatch")
class add_stories(CreateView):  # new
    model = Story
    form_class = StoryForm
    template_name = "addstories.html"
    success_url = '/'

# @login_required
# def add_stories(request):
#     form = StoryForm
#     if request.method == "POST":
#         if form.is_valid:
#             title = request.POST.get('title')
#             category = request.POST.get('category')
#             content = request.POST.get('content')
#             cover = request.POST.get('cover')
#             story_obj = Story(title = title, category = category, content = content, cover = cover)
#             story_obj.save()
#             return redirect('/')
#     return render(request, 'addstories.html',{ "form" :form})

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