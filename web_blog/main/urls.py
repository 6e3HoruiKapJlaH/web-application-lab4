from django.urls import path
from . import views
from django.conf import settings


#Урлы, которые обслуживает сервер
urlpatterns = [
    path('', views.index),

    path('contacts.html', views.contacts),


]
