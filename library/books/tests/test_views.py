from django.test import TestCase

from books.models import Book, Author

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


class ListAuthorViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for num in range(11):
            Author.objects.create(name=str(num),
                                  surname=str(num*2))

    def test_list_author(self):
        resp = self.client.get('/authors/')
        self.assertEqual(resp.status_code, 200)

    def test_detail_author(self):
        resp = self.client.get('/author/1/')
        self.assertEqual(resp.status_code, 200)


class CreateBookViewTest(TestCase):
    def test_create_book_get_view(self):
        resp = self.client.get('/add_new_book/')
        self.assertEqual(resp.status_code, 200, msg=resp.content)

    def test_create_book_post_view(self):
        resp = self.client.post('/add_new_book/', {'title': ['Test Book'], 'rate': [1]}, follow=True)
        self.assertEqual(resp.status_code, 200, msg=resp.content)


class CreateAuthorViewTest(TestCase):
    def test_create_author_get_view(self):
        resp = self.client.get('/add_new_author/')
        self.assertEqual(resp.status_code, 200, msg=resp.content)

    def test_create_author_post_view(self):
        resp = self.client.post('/add_new_author/', {'name': 'test', 'surname': 'Testor'}, follow=True)
        self.assertEqual(resp.status_code, 200, msg=resp.content)


class CreateGenreViewTest(TestCase):
    def test_create_genre_get_view(self):
        resp = self.client.get('/add_new_genre/')
        self.assertEqual(resp.status_code, 200, msg=resp.content)

    def test_create_author_post_view(self):
        resp = self.client.post('/add_new_genre/', {'name': 'test'}, follow=True)
        self.assertEqual(resp.status_code, 200, msg=resp.content)
