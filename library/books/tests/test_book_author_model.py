from django.test import TestCase

from books.models import Author, Book, Folder


class FolderTest(TestCase):

    def test_folder_create(self):
        folder = Folder.objects.create(name='First', size=9.5, created='2020-11-25')
        self.assertEquals(folder.name, 'First')

    def test_subfolder_create(self):
        main_parent_folder = Folder.objects.create(name='LocalLibraryBaseDir', size=1, created='2020-11-25')
        folder = Folder.objects.create(name='Main', size=1, created='2020-11-25', parent_folder=main_parent_folder)
        subfolder1 = Folder.objects.create(name='First', size=9.5, created='2020-11-25', parent_folder=folder)
        subfolder2 = Folder.objects.create(name='Second', size=1.5, created='2020-11-25', parent_folder=folder)

        self.assertEquals(len(folder.subfolders.all()), 2)
        self.assertEquals(subfolder2.parent_folder.name, 'Main')


class AuthorTest(TestCase):

    def test_author_create(self):
        author = Author(name='Thomas', surname='Piketty')
        author.save()
        self.assertEquals(author.name, 'Thomas')


class BookTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Author.objects.create(name='Thomas', surname='Pikkety')
        Folder.objects.create(name='LocalLibraryBaseDir', size=1, created='2020-11-25')

    def test_book_create(self):
        book = Book(title='Capital in the Twenty-First Century',
                    size=10, path='SomeFolder/AnotherFolder/Book.fb2',
                    file_creation_time='2020-11-24',
                    rate=5, have_read=True, is_favorite=True,
                    review='Very interesting', folder=Folder.objects.get(pk=1))
        book.save()
        self.assertIsInstance(book, Book)
        self.assertEquals(book.title, 'Capital in the Twenty-First Century')

    def test_book_relation_to_author(self):
        author = Author.objects.get(name='Thomas', surname='Pikkety')
        book = Book(title='Capital in the Twenty-First Century',
                    size=10, path='SomeFolder/AnotherFolder/Book.fb2',
                    file_creation_time='2020-11-24',
                    rate=5, have_read=True, is_favorite=True,
                    review='Very interesting', folder=Folder.objects.get(pk=1))
        book.save()
        book.author.add(author)
        book.save()
        related_author = book.author.all()[0]
        self.assertIsInstance(related_author, Author)
        self.assertEquals(related_author.name, 'Thomas')
        self.assertIsInstance(related_author.books.all()[0], Book)
        self.assertIsInstance(book.folder, Folder)
