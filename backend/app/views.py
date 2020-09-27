from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from datetime import datetime
from .models import Posting, Login, List_Book, Register
from .forms import LoginForm, BookForm, RegisterForm

def index(request): # detail view
    '''The app homepage'''
    posting_list = Posting.objects.all()
    template = loader.get_template('index.html')
    context = {
        'posting_list': posting_list,
        }
    return HttpResponse(template.render(context, request))

def about(request):
    '''A simple about us static page'''
    return HttpResponse('Not implemented')

def browse(request):
    '''A simple about us static page'''
    return HttpResponse('Not implemented')

def get_posting(request, posting_id):
    '''Display an existing posting'''
    return HttpResponse('Not implemented')

def create_posting(request):
    '''Send the create post template for a seller'''
    return HttpResponse('Not implemented')

def save_posting(request):
    '''Save the posting to the database'''
    #Parse the form? Model binding is a thing tho. 
    #Create the posting here
    return HttpResponse('Not implemented')

def login(request): 
    '''Login page'''
    context ={}
    template = loader.get_template('login.html')
    form = LoginForm(request.POST) 
    if form.is_valid(): 
        return HttpResponseRedirect("/") 
    context["form"] = form
    return HttpResponse(template.render(context, request))

def profile(request): 
    '''Profile page. Will replace hardcoded values with DB data'''
    name = "Jane Doe"
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


def register(request):
    '''Register a New User'''
    context ={}
    template = loader.get_template('register.html')
    form = RegisterForm(request.POST) 
    if form.is_valid(): 
        return HttpResponseRedirect("/") 
    context["form"] = form
    return HttpResponse(template.render(context, request))