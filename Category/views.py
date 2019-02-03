from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Bookstore import *
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from Category.models import Books, Author
from rest_framework import viewsets
from Category.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Category.models import *
from .serializers import *
from Bookstore.urls import *




# Create your views here.
@login_required(login_url="homepage")
def fiction(request):

    fictionbooks = {}
    f_books = Books.objects.all().filter(category__exact = 'fiction')
    fictionbooks["bookdata"] = f_books
    print(fictionbooks)

    return render(request, 'fiction.html',fictionbooks)
@login_required(login_url="homepage")
def horror(request):
    horrorbooks = {}
    h_books = Books.objects.all().filter(category__exact='horror')
    horrorbooks["bookdata"] = h_books


    # horrorbooks = { "data":["NOS4A2",
    #                         "Bloodchild",
    #                         "Lord Of The Flies",
    #                         "Beloved",
    #                         "Kindred"]}
    return render(request, 'horror.html',horrorbooks)
@login_required(login_url="homepage")
def suspense(request):
    suspensebooks = {}
    s_books = Books.objects.all().filter(category__exact='suspense')
    suspensebooks["bookdata"] = s_books

    # suspensebooks = { "data":["The Girl on the Train ",
    #                           "Before I Go To Sleep",
    #                           "Bird Box ",
    #                           "An Untamed State",
    #                           "Sphere "]}
    return render(request,'suspense.html',suspensebooks)
@login_required(login_url="homepage")
def delete_book(request,book_id):

    delete_data = Books.objects.get(id=book_id)
    delete_data.delete()
    return redirect("allbooks")

@login_required(login_url="homepage")
def delete_author(request, author_id):
    delete_data = Author.objects.get(id = author_id)
    delete_data.delete()
    return redirect("author")

@login_required(login_url="homepage")

def add_book(request):
    if request.method == 'POST':

        form = BookForm(request.POST)

        if form.is_valid():

            title = form.cleaned_data['title']
            category = form.cleaned_data['category']
            publisher = form.cleaned_data['publisher']
            language = form.cleaned_data['language']
            years = form.cleaned_data['years']
            rating_user = form.cleaned_data['rating_user']

            b =Books(title=title,category=category,publisher=publisher,language=language,years=years,rating_user=rating_user)
            b.save()
            return redirect("allbooks")

            print(title,category,publisher,language,years,rating_user)

    form = BookForm()

    return render(request, 'add_book.html', {'form':form})

@login_required(login_url="homepage")
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)

        if form.is_valid():

            author_fname = form.cleaned_data['author_fname']
            author_lname = form.cleaned_data['author_lname']
            rating_user = form.cleaned_data['rating_user']

            a = Author(author_fname=author_fname, author_lname=author_lname, rating_user=rating_user)
            a.save()
    form = AuthorForm()
    return render(request, 'add_author.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect("homepage")


# @login_required(login_url="homepage")
class assignauthor(TemplateView):
    login_required = True
    template_name = 'assign_author.html'

    def get(self,request):
        data_books = {}
        books = Books.objects.all()
        authordata = Author.objects.all()
        data_books["bookdata"] = books
        data_books["authordata"] = authordata
        # print(data_books)

        return render(request, "assign_author.html", data_books)

    def post(self, request):
        print(request.POST['bookid'])
        print(request.POST['authorid'])

        # b = Books.objects.get(title__exact = "title")
        # a =Author.objects.get(name__exact = "author_fname")
        b = Books.objects.get(id =request.POST['bookid'] )
        a =Author.objects.get(id = request.POST['authorid'])
        b.author = a
        b.save()

        return render(request, "assign_author.html")

class BookList(APIView):
    def get(self,request):
        books = Books.objects.all()
        serializer = BooksSerializer(books, many = True)
        return Response(serializer.data)

class AuthorList(APIView):
    def get(self,request):
        author = Author.objects.all().order_by('rating_user')
        serializer = AuthorSerializer(author, many = True)
        return Response(serializer.data)















# a = Author(author_fname = 'Raj', author_lname= 'Shah', rating_user = '4')
# a = Author(author_fname = 'Yash', author_lname= 'Patel', rating_user = '5')
# a = Author(author_fname = 'John', author_lname= 'Smith', rating_user = '3')
# a = Author(author_fname = 'Sahib', author_lname= 'Malhotra', rating_user = '4.5')
# a = Author(author_fname = 'Rahul', author_lname= 'Jani', rating_user = '2')
# a.save()
#
#
# b = Books(title = 'Anna Karenina', category ='fiction',publisher='ABC',language='english',years = '1995-01-12',rating_user= '4')
# b1 = Books(title = 'Madame Bovary', category ='fiction',publisher='DEF',language='english',years = '1990-08-19',rating_user= '3')
# b2 = Books(title = 'Bloodchild', category ='horror',publisher='XYZ',language='english',years = '1980-09-20',rating_user= '4.5')
# b3 = Books(title = 'Lord Of The Flies', category ='horror',publisher='PQR',language='english',years = '1985-03-17',rating_user= '4.5')
# b4 = Books(title = 'The Girl on the Train', category ='suspense',publisher='GEF',language='english',years = '2000-10-30',rating_user= '3')
# b5 = Books(title = 'Sphere', category ='horror',publisher='ABCD',language='english',years = '2004-05-17',rating_user= '4')
# b.save()
# b1.save()
# b2.save()
# b3.save()
# b4.save()
# b5.save()