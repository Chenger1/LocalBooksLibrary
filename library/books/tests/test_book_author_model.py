from django.test import TestCase

from books.models import Author, Book


class AuthorTest(TestCase):

    def test_author_create(self):
        author = Author(name='Thomas', surname='Piketty')
        author.save()
        self.assertEquals(author.name, 'Thomas')


class BookTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Author.objects.create(name='Thomas', surname='Pikkety')

    def test_book_create(self):
        book = Book(title='Capital in the Twenty-First Century',
                    size=10, path='SomeFolder/AnotherFolder/Book.fb2',
                    time_of_adding_to_system='2020-11-24',
                    rate=5, have_read=True, is_favorite=True,
                    review='Very interesting')
        book.save()
        self.assertIsInstance(book, Book)
        self.assertEquals(book.title, 'Capital in the Twenty-First Century')

    def test_book_relation_to_author(self):
        author = Author.objects.get(name='Thomas', surname='Pikkety')
        book = Book(title='Capital in the Twenty-First Century',
                    size=10, path='SomeFolder/AnotherFolder/Book.fb2',
                    time_of_adding_to_system='2020-11-24',
                    rate=5, have_read=True, is_favorite=True,
                    review='Very interesting')
        book.save()
        book.author.add(author)
        book.save()
        related_author = book.author.all()[0]
        self.assertIsInstance(related_author, Author)
        self.assertEquals(related_author.name, 'Thomas')
        self.assertIsInstance(related_author.books.all()[0], Book)
