"""Bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from Bookstore import views
from django.contrib import admin
from Category import views as catview
from Category.views import *
from rest_framework import routers
from rest_framework.urlpatterns import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('bjson/',BookList.as_view(),name = "bjson"),
    path('ajson/',AuthorList.as_view(),name = "ajson"),
    path('admin/', admin.site.urls),
    path('', views.homepage,name="homepage"),
    path('contactus/',views.contactus),
    path('books/', views.books,name="allbooks"),
    path('author/',views.author, name = "author"),
    path('books/', include('Category.urls')),
    path('books/delete/<int:book_id>', catview.delete_book,name="del"),
    path('author/delete/<int:author_id>', catview.delete_author, name="del_author"),
    path('addbook/', catview.add_book,name="add_book"),
    path('addauthor/', catview.add_author, name="addauthor"),
    path('logout/', catview.logout_view,name="logout_view"),
    path('assignauthor/', login_required(assignauthor.as_view()),name = "assignauthor"),
    # path('assignauthor/<int:book_id>',catview.assignauthor.as_view,name = "assignauthor")
]
urlpatterns = format_suffix_patterns(urlpatterns)