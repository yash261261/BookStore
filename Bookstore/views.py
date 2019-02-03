from django.http import HttpResponse
from django.shortcuts import render
from Category.models import *
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login,logout

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def homepage(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # print(username, password)
        if User.objects.filter(username=username).exists():
            login(request, user)
            return redirect("allbooks")
            # return render(request, 'books.html')
        else:
            return HttpResponse("<h1>Invalid Details</h1>")
    else:
        return render(request, 'homepage.html')
    # return render(request,'homepage.html')\

@login_required(login_url="homepage")
def contactus(request):
    return HttpResponse ("<h1>You can reach us at 123-456-7890</h1>")


@login_required(login_url="homepage")
def books(request):
    mydata={}
    books=Books.objects.all()
    mydata["bookdata"]=books


    return render(request,'books.html',mydata)

@login_required(login_url="homepage")
def author(request):
    data = {}
    author = Author.objects.all()
    data["authordata"]=author

    return render(request, 'author.html', data)
