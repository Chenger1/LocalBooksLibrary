from django.test import TestCase

from books.models import Book

import random


class ListBookViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        for num in range(11):
            Book.objects.create(title=str(num), rate=1,
                                is_favorite=bool(random.randint(0, 1)),
                                to_read=bool(random.randint(0, 1)),
                                have_read=bool(random.randint(0, 1)))

    def test_list_book_view(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200, msg=resp.content)


class ListFavoriteBookViewTest(ListBookViewTest, TestCase):
    def test_list_favorite_book(self):
        resp = self.client.get('/is_favorite/')
        for book in resp.context_data['book_list']:
            self.assertEqual(book.is_favorite, True)


class ListToReadBookViewTest(ListBookViewTest, TestCase):
    def test_list_to_read_book(self):
        resp = self.client.get('/to_read/')
        for book in resp.context_data['book_list']:
            self.assertEqual(book.to_read, True)


class ListHaveReadBookViewTest(ListBookViewTest, TestCase):
    def test_list_have_read_book(self):
        resp = self.client.get('/have_read/')
        for book in resp.context_data['book_list']:
            self.assertEqual(book.have_read, True)
