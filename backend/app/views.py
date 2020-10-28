import os
import json
from itertools import chain
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
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
from .forms import BookForm, ReportForm
from .models import Posting, List_Book, Register, Favorite, Message
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.urls import reverse

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

def my_postings(request):
    '''Displays a list of the logged in user\'s books for sale'''
    context = {'postings': Posting.objects.filter(seller=request.user)}
    template = loader.get_template('my_postings.html')
    return HttpResponse(template.render(context, request))

def get_posting(request, posting_id):
    '''Display an existing posting'''
    template = loader.get_template('posting.html')

    # Get data from DB
    posting = model_to_dict(Posting.objects.get(id=posting_id))
    book = model_to_dict(List_Book.objects.get(id=posting['book']))
    seller = model_to_dict(User.objects.get(id=posting['seller']))['username']
    seller_id = model_to_dict(User.objects.get(id=posting['seller']))['id']

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
        "book_thumbnail": book_thumbnail,
        "seller_id": seller_id
    }
    return HttpResponse(template.render(context, request))


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
        
        if len(isbn) == 0:
            isbn = 'N/A'
        
        if '' in (title, author, subject, class_used, des, price):
            return HttpResponse(template.render({'error': 'Please fill out all fields.'}, request))

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


def register(request):
    '''Register a New User'''
    template = loader.get_template('register.html')
    if request.POST:
        if User.objects.filter(username=request.POST['username']).count() == 0:

            # check for SJSU email
            err = False
            email = request.POST['email']
            if len(email) >= 10:
                if email[-9:] != "@sjsu.edu":
                    err = True
            else:
                err = True

            if err:
                context = {
                    'error': 'Please supply a SJSU email.'
                }
                return HttpResponse(template.render(context, request))

            # check for proper pw
            pw = request.POST['password']
            # idea form: https://stackoverflow.com/questions/17140408/if-statement-to-check-whether-a-string-has-a-capital-letter-a-lower-case-letter/17140466
            spec = set("!#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
            rules = [
                lambda l: any(c.isupper() for c in pw) or 'no_upper',
                lambda l: any(c.isdigit() for c in pw) or 'no_digit',
                lambda l: any(c in spec for c in pw) or 'no_special',
                lambda l: len(pw) >= 10 or 'length'
            ]
            res = [p for p in [r(pw) for r in rules] if p != True]
            if len(res) > 0:
                context = {
                    'error': 'Passwords must be at least 10 characters long, with at least one special character and uppercase character'
                }
                return HttpResponse(template.render(context, request))

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

def report(request, posting_id):
    '''Handle reporting of a posting'''
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login")

    try:
        posting = Posting.objects.get(pk=posting_id)
    except:
        return render(request, 'report.html', {'error': 'Posting does not exist'})

    if request.method == 'POST':
        form = ReportForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.posting = posting
            instance.posting_snapshot = json.dumps(model_to_dict(posting))
            instance.save()
            return HttpResponseRedirect(reverse('posting', args=[posting.id]) + '?reported=1')
    else:
        form = ReportForm()

    return render(request, 'report.html', {'form': form})

def chat(request, other_user_id=None, posting_id=None):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login")
    if other_user_id is None:
        template = loader.get_template('all_chats.html')
        rs = Message.objects.filter(Q(to_user=request.user)|Q(from_user=request.user)).values_list('to_user', 'from_user').distinct()
        other_user_set = set()
        for to_id, from_id in rs:
            if to_id != request.user.id:
                other_user_set.add(to_id)
            if from_id != request.user.id:
                other_user_set.add(from_id)
        msg_infos = []
        for other_user_id in other_user_set:
            other_user = User.objects.get(id=other_user_id)
            other_profile_pic = f'{settings.MEDIA_URL}/profile_pics/{other_user_id}.jpg'
            msg_count = Message.objects.filter(from_user_id=other_user, to_user=request.user).count()
            msg_count += Message.objects.filter(to_user_id=other_user, from_user=request.user).count()
            last_msg_preview = Message.objects.filter(from_user=other_user, to_user=request.user).order_by('-id').first()
            if last_msg_preview is not None:
                last_msg_preview = last_msg_preview.message_text
                last_msg_preview = last_msg_preview[0:20]  + "...."
            msg_infos.append({
                'other_user' : other_user,
                'msg_count'  : msg_count,
                'last_msg_preview'  : last_msg_preview,
                'other_profile_pic': other_profile_pic
            })
        context = {                
            'msg_infos': msg_infos 
        }
        return HttpResponse(template.render(context, request))
    if int(other_user_id) == int(request.user.id):
        #You cant message yourself...
        return HttpResponseRedirect("/")
    is_first_msg = False
    if posting_id is not None and \
       Message.objects.filter(from_user=request.user, to_user=other_user_id).count() == 0:
        #We only get the conversation started for the first msg
        initial_msg = Message(from_user=request.user, to_user_id=other_user_id, 
            message_text=f'Hi there! I\'m interested in buying {Posting.objects.get(id=posting_id).title}')
        initial_msg.save()
        is_first_msg = True
    template = loader.get_template('chat.html')
    to_user = User.objects.get(id=other_user_id)
    my_profile_pic = f'{settings.MEDIA_URL}/profile_pics/{request.user.id}.jpg'
    other_profile_pic = f'{settings.MEDIA_URL}/profile_pics/{other_user_id}.jpg'
    context = {
        'to_user':  to_user,
        'my_profile_pic': my_profile_pic,
        'other_profile_pic': other_profile_pic,
        'is_first_msg': is_first_msg
    }

    return HttpResponse(template.render(context, request))

@csrf_exempt
def message(request, other_user_id):
    if request.POST:
        #add the form data from the request to db
        msg = Message(from_user=request.user, to_user_id=other_user_id, message_text=request.POST['message_text'])
        msg.save()
        return HttpResponse('OK')
    else:
        #Get all messages between the two users 
        other_user = User.objects.get(id=other_user_id)
        messages = {
            'messages': []
        }
        from_to = Message.objects.filter(from_user=request.user, to_user_id=other_user_id)
        to_from = Message.objects.filter(to_user=request.user, from_user_id=other_user_id)
        for msg in from_to:
            msg = model_to_dict(msg)
            msg['from_user'] = 'Me:'
            messages['messages'].append(msg)

        for msg in to_from:
            msg = model_to_dict(msg)
            msg['from_user'] = f'{other_user.username}:'
            messages['messages'].append(msg)

        messages['messages'].sort(key=lambda m: m['id'])


        json_messages = json.dumps(messages)

        return HttpResponse(json_messages)
