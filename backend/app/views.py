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
    for i in range(len(posting_list)):
        # Right now only supports png, we need to use a regex here instead
        img = finders.find(f'img/book_thumbnails/{posting_list[i].id}.png')
        if img is not None:
            img = img.split('/static/')[1]

        posting_image_list.append((posting_list[i], img))

    template = loader.get_template('browse.html')
    context = {
        'posting_image_list': posting_image_list,
        'user_favorites_list': get_favorites(request.user),
    }
    return HttpResponse(template.render(context, request))


def get_posting(request, posting_id):
    '''Display an existing posting'''
    template = loader.get_template('posting.html')
    posting = Posting.objects.get(id=posting_id)
    img = finders.find(f'img/book_thumbnails/{posting_id}.png')
    favorites = get_favorites(request.user)
    if img is not None:
        img = img.split('/static/')[1]

    context = {
        "posting": posting,
        "image": img,
        "user_favorites_list": favorites
    }

    return HttpResponse(template.render(context, request))

    return HttpResponse('Not implemented')


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
        # title = request.POST['title']
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        subject = request.POST.get('subject')
        class_used = request.POST.get('class_used')
        des = request.POST.get('description')
        price = request.POST.get('price')
        if '' in (title, author, isbn, subject, class_used, des, price):
            return HttpResponse(template.render({'error': 'Please fill out all fields.'}, request))
        else:
            # Post to Posting and List_Book
            book = List_Book(title=title,author=author,isbn=isbn,subject=subject,class_used=class_used)
            book.save()
            posting = Posting(title=title,price=price,description=des,book_id=book.id,buyer_id=1,seller_id=request.user.id)
            posting.save()

            return redirect('view_book', book_id=book.id)


            # template = loader.get_template('view_book');
            # return HttpResponse(template.render({'posting': posting}, request))
    else:
        return HttpResponse(template.render({}, request))

def view_book(request, book_id):
    '''
    Book page. Will replace hardcoded values with DB data
    Book ID will be used to query for data
    '''
    # name = "Structure and Interpretation of Computer Programs"
    # author = "Harold Abelson, Gerald Jay Sussman, Julie Sussman"
    # isbn = "0-262-51087-1"
    # subject = "Computer Science"
    # class_used = "CS146"
    # template = loader.get_template('book_view.html')
    # context = {
    #     'name': name,
    #     'author': author,
    #     'isbn': isbn,
    #     'subject': subject,
    #     'class_used': class_used
    # }
    book_id_rn = book_id
    template = loader.get_template('book_view.html')
    book = List_Book.objects.get(pk=book_id)
    post = Posting.objects.filter(book_id=book_id)
    print("*****")
    print(post)
    print(book)
    print("******")
    return HttpResponse(template.render({}, request))


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