from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from Category.models import *
from django.contrib.auth import authenticate, get_user_model,login, logout

class BookForm(forms.Form):
    title = forms.CharField(max_length=50)
    category = forms.CharField(max_length=50)
    publisher = forms.CharField(max_length=50)
    language = forms.CharField(max_length=50)
    years = forms.DateField()
    rating_user = forms.FloatField()


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['author_fname', 'author_lname', 'rating_user']

form = AuthorForm()




