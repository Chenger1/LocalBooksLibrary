from django.test import TestCase

from books.models import Book, Author


class BookTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(name='Legendary', surname='Author')

    def test_create_book(self):
        book = Book(title='Capital in the Twenty-First Century',
                    rate=5, have_read=True, is_favorite=True,
                    review='Very interesting',)
        book.save()
        self.assertIsInstance(book, Book)
        self.assertEquals(book.title, 'Capital in the Twenty-First Century')

    def test_book_relation_to_author(self):
        book = Book(title='Capital in the Twenty-First Century',
                    rate=5, have_read=True, is_favorite=True,
                    review='Very interesting', )
        book.save()
        book.author.add(self.author)
        book.save()
        related_author = book.author.all()[0]
        self.assertIsInstance(related_author, Author)
        self.assertEquals(related_author.name, 'Legendary')
        self.assertIsInstance(related_author.books.all()[0], Book)
