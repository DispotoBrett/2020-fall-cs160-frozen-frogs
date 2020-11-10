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
        List_Book.objects.create(
            title='Hello World',
            author='Bob Smith',
            isbn='123456789',
            subject='Computer Programming',
            class_used='CS49J'
        )

    def test_book_exists(self):
        book = List_Book.objects.get(title='Hello World')
        self.assertIs(book is not None, True)
