from django.contrib import admin
from django.urls import path,include
from defaultapp import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about , name = 'about'),
    path('services', views.services , name = 'services'),
    path('maggamblouses', views.maggamblouses, name = 'maggamblouses'),
    path('designblouses', views.designblouses, name = 'designblouses'),
    path('contact', views.contact , name = 'contact'),
    path('signin', views.signin, name = 'signin'),
    path('signup', views.signup, name = 'signup'),
    
]