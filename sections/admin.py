from django.contrib import admin

# Register your models here.
from sections.models import Skill, Story

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    pass