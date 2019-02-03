from django.conf.urls import re_path
from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [

    path("fiction/",views.fiction, name= 'fiction'),
    path("horror/",views.horror,name='horror'),
    path("suspense/",views.suspense,name='suspense')
]