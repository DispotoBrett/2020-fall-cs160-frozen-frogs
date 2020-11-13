from django.contrib.auth.models import User
from django.test import TestCase
from unittest import TestCase as UnitTestCase

from app.models import *

# Note: Once tests start accumulating in this file, it is a good practice
# to make tests its own python package (i.e. directory) for organization

# Note: Tests involving database access should inherit from django.test.TestCase
# Others may use UnitTest

# Note: A temporary database is used when running tests and it is disposed of
# after tests have finished running


class ListBookTestCase(TestCase):
    def setUp(self):
        book = create_test_book()
        self.book_pk = book.pk

    def test_book_exists(self):
        book = List_Book.objects.get(pk=self.book_pk)
        self.assertIs(book is not None, True)

    def test_update_book(self):
        author_name = 'Bob Smith Jr'

        book = List_Book.objects.get(pk=self.book_pk)
        book.author = author_name
        book.save()

        updated_book = List_Book.objects.get(pk=self.book_pk)
        self.assertEqual(updated_book.author, author_name)


class PostingTestCase(TestCase):
    def setUp(self):
        user = create_test_user()
        book = create_test_book()
        posting = create_test_posting(user, book)

        self.posting_pk = posting.pk

    def test_posting_exists(self):
        posting = Posting.objects.get(pk=self.posting_pk)
        self.assertIs(posting is not None, True)


class FavoriteTestCase(TestCase):
    def setUp(self):
        self.user = create_test_user()
        self.book = create_test_book()
        self.posting = create_test_posting(self.user, self.book)

    def test_create_favorite(self):
        favorite = Favorite.objects.create(user=self.user, posting=self.posting)
        self.assertIs(favorite is not None, True)


class MessageTestCase(TestCase):
    def setUp(self):
        user1 = create_test_user()
        user2 = create_test_user(name='tester2')
        message = Message.objects.create(
            to_user=user2,
            from_user=user1,
            message_text='Hi there! I would like to purchase your book'
        )

        self.message_pk = message.pk

    def test_message_exists(self):
        message = Message.objects.get(pk=self.message_pk)
        self.assertIs(message is not None, True)


class RegisterTestCase(TestCase):
    def test_create_register(self):
        register = Register.objects.create(
            sjsu_id=12345678,
            sjsu_pw='12345678',
            name='test account'
        )
        self.assertIs(register is not None, True)


class ReportTestCase(TestCase):
    def setUp(self):
        self.user = create_test_user()
        self.book = create_test_book()
        self.posting = create_test_posting(self.user, self.book)

    def test_create_report(self):
        report = Report.objects.create(
            user=self.user,
            posting=self.posting,
            description='Testing the reporting feature',
            posting_snapshot=''
        )
        self.assertIs(report is not None, True)


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
