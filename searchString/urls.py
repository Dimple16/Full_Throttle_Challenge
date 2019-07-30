from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^checkdata', views.checkdata, name = 'checkdata'),
    url(r'^getform', views.getFormdata, name='getFormdata'),
]