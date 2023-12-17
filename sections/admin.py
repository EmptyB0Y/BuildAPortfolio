from django.contrib import admin

# Register your models here.
from sections.models import Skill, Story, Shooting, Photo

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Shooting)
class ShootingAdmin(admin.ModelAdmin):
    pass

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass