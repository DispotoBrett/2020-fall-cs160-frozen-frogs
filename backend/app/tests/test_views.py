from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase
from django.urls import reverse
from http import HTTPStatus

from app.views import *
from .utils import create_test_user


class IndexViewTestCase(TestCase):
    def test_get(self):
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Welcome to Spartan Bookshare!', html=True)


class BrowseViewTestCase(TestCase):
    def test_get(self):
        response = self.client.get(reverse('browse'))

        self.assertEqual(response.status_code, HTTPStatus.OK)


class AboutUsViewTestCase(TestCase):
    def test_get(self):
        response = self.client.get(reverse('aboutus'))

        self.assertEqual(response.status_code, HTTPStatus.OK)


class RegisterViewTestCase(TestCase):
    def test_get(self):
        response = self.client.get(reverse('register'))

        self.assertEqual(response.status_code, HTTPStatus.OK)


class LoginViewTestCase(TestCase):
    def test_get(self):
        response = self.client.get(reverse('login'))

        self.assertEqual(response.status_code, HTTPStatus.OK)


# Logged in view tests


class LogoutViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = create_test_user()

    def test_get(self):
        request = self.factory.get(reverse('logout'))
        request.user = self.user

        response = logout_view(request)

        self.assertEqual(response.status_code, HTTPStatus.OK)


class ProfileViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = create_test_user()

    def test_get(self):
        request = self.factory.get(reverse('profile'))
        request.user = self.user

        response = profile(request)

        self.assertEqual(response.status_code, HTTPStatus.OK)


class MyPostingsViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = create_test_user()

    def test_get(self):
        request = self.factory.get(reverse('my_postings'))
        request.user = self.user

        response = my_postings(request)

        self.assertEqual(response.status_code, HTTPStatus.OK)


class ListBookViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        request = self.factory.get(reverse('list_book'))
        request.user = AnonymousUser()

        response = list_book(request)

        self.assertEqual(response.status_code, HTTPStatus.OK)


class ChatViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = create_test_user()

    def test_get(self):
        request = self.factory.get(reverse('chat'))
        request.user = self.user

        response = chat(request)

        self.assertEqual(response.status_code, HTTPStatus.OK)
