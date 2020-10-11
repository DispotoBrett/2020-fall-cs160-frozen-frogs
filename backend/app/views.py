from time import sleep
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from datetime import datetime
from .models import Posting
from django.contrib.staticfiles import finders
from .models import Posting, List_Book, Register
from .forms import BookForm, RegisterForm
from django.contrib.auth import logout

def index(request): # detail view
    '''The app homepage'''
    posting_list = Posting.objects.all()
    template = loader.get_template('index.html')
    context = {
        'posting_list': posting_list[0:5],
        }
    return HttpResponse(template.render(context, request))

def browse(request):
    '''A more detailed version of the homepage book listing'''
    posting_list = Posting.objects.all()
    posting_image_list = []
    for i in range(len(posting_list)):
        #Right now only supports png, we need to use a regex here instead
        img = finders.find(f'img/book_thumbnails/{posting_list[i].id}.png')
        if img is not None:
            img = img.split('/static/')[1]

        posting_image_list.append((posting_list[i] , img))
        
    template = loader.get_template('browse.html')
    context = {
        'posting_image_list': posting_image_list,
        }
    return HttpResponse(template.render(context, request))

def get_posting(request, posting_id):
    '''Display an existing posting'''
    template = loader.get_template('posting.html')
    posting = Posting.objects.get(id=posting_id)
    img = finders.find(f'img/book_thumbnails/{posting_id}.png')
    if img is not None:
        img = img.split('/static/')[1]

    context = {
        "posting" : posting,
        "image" : img
    } 

    return HttpResponse(template.render(context, request))


    return HttpResponse('Not implemented')

def create_posting(request):
    '''Send the create post template for a seller'''
    return HttpResponse('Not implemented')

def save_posting(request):
    '''Save the posting to the database'''
    #Parse the form? Model binding is a thing tho. 
    #Create the posting here
    return HttpResponse('Not implemented')

def profile(request): 
    '''Profile page. Will replace hardcoded values with DB data'''
    if not request.user.is_authenticated:
        #TODO Redirct 
        name = "Not Logged In"
    else:
        name =request.user.username
    email = "jane.doe@sjsu.edu"
    template = loader.get_template('profile.html')
    context = {
    	'name': name,
    	'email': email
    }
    return HttpResponse(template.render(context, request))

def list_book(request):
    '''Form for listing a book for sale'''
    context ={}
    template = loader.get_template('list_book.html')
    form = BookForm(request.POST) 
    if form.is_valid(): 
        return HttpResponseRedirect("/") 
    context["form"] = form
    return HttpResponse(template.render(context, request))

def view_book(request, book_id): 
    '''
    Book page. Will replace hardcoded values with DB data
    Book ID will be used to query for data
    '''
    name = "Structure and Interpretation of Computer Programs"
    author = "Harold Abelson, Gerald Jay Sussman, Julie Sussman"
    isbn = "0-262-51087-1"
    subject = "Computer Science"
    class_used = "CS146"
    template = loader.get_template('book_view.html')
    context = {
        'name': name,
        'author': author,
        'isbn': isbn,
        'subject': subject,
        'class_used': class_used
    }
    return HttpResponse(template.render(context, request))

def register(request):
    '''Register a New User'''
    context ={}
    template = loader.get_template('register.html')
    form = RegisterForm(request.POST) 
    if form.is_valid(): 
        return HttpResponseRedirect("/") 
    context["form"] = form
    return HttpResponse(template.render(context, request))

def logout_view(request):
    logout(request)
    return index(request) 