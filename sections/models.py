from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=500)

CATEGORY = (
    ("Technology", "Technology"),
    ("Data Science", "Data Science"),
    ("Database", "Database"),
    ("Security", "Security"),
    ("Web Dev", "Web dev"),
    ("Machine learning", "Machine learning")
    )

class Story(models.Model):
    title = models.CharField(max_length= 100)
    category = models.CharField(choices= CATEGORY,max_length=30, default= "Technology")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)

   
    def __str__(self):
        return self.title