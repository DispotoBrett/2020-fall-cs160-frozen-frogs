from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from .models import Posting


def index(request):
    '''The app homepage'''
    posting_list = Posting.objects.all()
    template = loader.get_template('index.html')
    context = {
        'posting_list': posting_list,
        }
    return HttpResponse(template.render(context, request))


def get_posting(request, posting_id):
    '''Display an existing posting'''
    return HttpResponse()


def create_posting(request):
    '''Send the create post template for a seller'''
    return HttpResponse('Create posting form goes here')


def save_posting(request):
    '''Save the posting to the database'''
    #Parse the form? Model binding is a thing tho. 
    #Create the posting here
    return HttpResponse('Success or failure')


def profile(request): 
	name = "Jane Doe"
	email = "jane.doe@sjsu.edu"
	context = {
		'name': name,
		'email': email
	}
	return render(request, 'profile.html', context)
