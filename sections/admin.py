from django.contrib import admin

# Register your models here.
from sections.models import Skill, Story, Shooting, Photo, TitlePane

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

@admin.register(TitlePane)
class TitlePaneAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(TitlePaneAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['image'].required = False
        return form