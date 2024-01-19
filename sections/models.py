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
    cover = models.ImageField(upload_to='images/', null=True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)

   
    def __str__(self):
        return self.title
    

class Shooting(models.Model):
    title = models.CharField(max_length= 100)
    cover = models.ImageField(upload_to='images/', null=True)
    order = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)

   
    def __str__(self):
        return self.title

class Photo(models.Model):
    title = models.CharField(max_length= 100)
    image = models.ImageField(upload_to='images/', null=True)
    shooting = models.ForeignKey(Shooting, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.title
    
class TitlePane(models.Model):
    content = models.CharField(max_length= 100)
    redirectLink = models.CharField(max_length= 100, default='/')
    image = models.ImageField(upload_to='images/', null=True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.content