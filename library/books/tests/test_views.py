from django.test import TestCase

from books.models import Book

import random


class ListBookViewTest(TestCase):
    def test_list_book_view(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200, msg=resp.content)


class ListFavoriteBookViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        for num in range(10):
            Book.objects.create(title=str(num), rate=1,
                                is_favorite=bool(random.randint(0, 1)))

    def test_list_favorite_book(self):
        resp = self.client.get('/is_favorite/')
        for book in resp.context_data['book_list']:
            self.assertEqual(book.is_favorite, True)
