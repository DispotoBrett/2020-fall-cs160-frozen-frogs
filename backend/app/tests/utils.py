from django.contrib.auth.models import User

from app.models import *


def create_test_user(name='tester'):
    user = User.objects.create_user(
        username=name,
        password='{name}123456',
        email='{name}@spam.la'
    )
    return user


def create_test_book():
    book = List_Book.objects.create(
        title='Hello World',
        author='Bob Smith',
        isbn='123456789',
        subject='Computer Programming',
        class_used='CS49J'
    )
    return book


def create_test_posting(user, book):
    posting = Posting.objects.create(
        title='Intro to Programming',
        price=50,
        description='Used programming book for sale',
        seller=user,
        buyer=user,
        book=book
    )
    return posting