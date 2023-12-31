"""BuildAPortfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include
from django.contrib import admin
from django.urls import path
from sections import views as sectionsViews
from django.conf import settings  # new
from django.conf.urls.static import static  # new
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('', sectionsViews.base),
    path('stories/', sectionsViews.mosaic),
    path('shootings/', sectionsViews.mosaic_photos),
    path('shooting/<int:id>/', sectionsViews.shooting_mosaic, name="shooting"),
    path('story/<int:id>/',sectionsViews.story, name="story"),
    path('addstories/', sectionsViews.add_stories.as_view()),
    path('addskills/', sectionsViews.add_skills),
    path('addshootings/', sectionsViews.add_shooting),
    path('addphotos/<int:shootingId>', sectionsViews.add_photos)
]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)