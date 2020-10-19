import os
from .utils import upload_img, get_favorites
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from time import sleep
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from datetime import datetime
from django.contrib.staticfiles import finders
from .models import Posting, List_Book, Register, Favorite
from .forms import BookForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.forms.models import model_to_dict

def index(request):  # detail view
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
    if request.user.is_authenticated:
        favorites_list = get_favorites(request.user)
    else:
        favorites_list =  []
    for i in range(len(posting_list)):
        # Right now only supports png, we need to use a regex here instead
        img = f'{settings.MEDIA_URL}/listing_photos/{posting_list[i].id}.jpg'
        posting_image_list.append((posting_list[i], img))

    template = loader.get_template('browse.html')
    context = {
        'posting_image_list': posting_image_list,
        'user_favorites_list': favorites_list,
    }
    return HttpResponse(template.render(context, request))


def get_posting(request, posting_id):
    '''Display an existing posting'''
    template = loader.get_template('posting.html')

    # Get data from DB
    posting = model_to_dict(Posting.objects.get(id=posting_id))
    book = model_to_dict(List_Book.objects.get(id=posting['book']))
    seller = model_to_dict(User.objects.get(id=posting['seller']))['username']

    # Get favorites
    if request.user.is_authenticated:
        favorites = get_favorites(request.user)
    else:
        favorites = []

    book_thumbnail = f'{settings.MEDIA_URL}/listing_photos/{book["id"]}.jpg'

    # Generate context
    context = {
        "posting": posting,
        "book": book,
        "user_favorites_list": favorites,
        "seller": seller,
        "book_thumbnail": book_thumbnail
    }
    return HttpResponse(template.render(context, request))


def create_posting(request):
    '''Send the create post template for a seller'''
    return HttpResponse('Not implemented')


def save_posting(request):
    '''Save the posting to the database'''
    # Parse the form? Model binding is a thing tho.
    # Create the posting here
    return HttpResponse('Not implemented')


def profile(request):
    '''Profile page. Will replace hardcoded values with DB data'''
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")
    user_favorites_list = get_favorites(request.user)
    favorites = []
    for record in user_favorites_list:
        favorites.append(Posting.objects.get(id=record))
    profile_pic = f'{settings.MEDIA_URL}/profile_pics/{request.user.id}.jpg'
    name = request.user.username
    email = request.user.email
    template = loader.get_template('profile.html')
    context = {
        'name': name,
        'email': email,
        'profile_pic': profile_pic,
        'favorites': favorites,
        'user_favorites_list': user_favorites_list, #for the shared actions list
    }
    return HttpResponse(template.render(context, request))


def list_book(request):
    '''Form for listing a book for sale'''
    template = loader.get_template('list_book.html')
    if request.POST:
        
        # Get data from form
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        subject = request.POST.get('subject')
        class_used = request.POST.get('class_used')
        des = request.POST.get('description')
        price = int(request.POST.get('price'))


        # Check if all fields filled in
        if '' in (title, author, isbn, subject, class_used, des, price):
            return HttpResponse(template.render({'error': 'Please fill out all fields.'}, request))

        # check if int
        if not isinstance(price, int):
            return HttpResponse(template.render({'error': 'Please choose a numeric price.'}, request))
        else:
            # Post to Posting and List_Book
            book = List_Book(title=title,author=author,isbn=isbn,subject=subject,class_used=class_used)
            book.save()
            posting = Posting(title=title,price=price,description=des,book=book,buyer=request.user,seller=request.user)
            posting.save()

            profile_pic = request.FILES['picture']
            upload_img(profile_pic, f'listing_photos/{book.id}.jpg')

            return redirect('posting', posting_id=posting.id)
    else:
        return HttpResponse(template.render({}, request))

# DEPRECATED --- use get_posting instead
# def view_book(request, book_id):
#     '''
#     Book page. Will replace hardcoded values with DB data
#     Book ID will be used to query for data
#     '''
#     book_id_rn = book_id
#     template = loader.get_template('book_view.html')
#     book = List_Book.objects.filter(id=book_id)
#     post = Posting.objects.filter(book_id=book_id)
#     book_data = str(book[0]).split(',')
#     posting_data = str(post[0]).split(',')
#     context = {
#         'name': posting_data[0],
#         'author': book_data[1],
#         'isbn': book_data[2],
#         'subject': book_data[3],
#         'class_used': book_data[4],
#         'price': posting_data[1],
#         'des': posting_data[2]
#     }
#     return HttpResponse(template.render(context, request))


def register(request):
    '''Register a New User'''
    template = loader.get_template('register.html')
    if request.POST:
        if User.objects.filter(username=request.POST['username']).count() == 0:
            new_user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            new_user.save()
            login(request, new_user)
            profile_pic = request.FILES['picture']
            #The form only accepts jpg 
            upload_img(profile_pic, f'profile_pics/{new_user.id}.jpg')
            return HttpResponseRedirect("/profile")
        else:
            context = {
                'error': f'Username {request.POST["username"]} already exists'
            }
            return HttpResponse(template.render(context, request))
    else:
        context = {'error': None}
        return HttpResponse(template.render(context, request))

# Weird name because of name conflicts with django login
def login_view(request):
    template = loader.get_template('login.html')
    logout(request)
    if request.POST:
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/profile")
        else:
            context = {
                'auth_failed': True
            }
            return HttpResponse(template.render(context, request))
    else:
        context = {
            'auth_failed': False
        }
        return HttpResponse(template.render(context, request))

# Weird name because of name conflicts with django logout
def logout_view(request):
    logout(request)
    return index(request)


def favorite(request, posting_id):
    if request.user.is_authenticated:
        is_favorited = Favorite.objects.filter(posting_id=posting_id, user=request.user)
        if is_favorited.count() > 0:
            is_favorited.delete()
        else:
            favorite = Favorite(user=request.user,  posting_id=posting_id)
            favorite.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return HttpResponseRedirect("/login")