"""tacocat_mainapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#i might have to use include here, check the live project for arguements
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # the 'name=' has to match the url tag in html file
    path('concept/', views.concept, name='concept'),
    path('scoreboard/', views.scoreboard, name='scoreboard'),
    # path('join/', views.join, name='join'),
    path('bacon_sausage/', views.bacon_sausage, name='bacon_sausage'),
    path('join/', include('Users.urls')),
    path('topics/', include('Items.urls')),
]


