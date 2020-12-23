from books.models import Folder, Author, Book

from book_finder.services.finder import Directory
from book_finder.services.finder import Book as BookClass


class Saver:

    @classmethod
    def save_structure_to_db(cls, directory: Directory, parent_folder: Folder = None) -> dict:
        new_folder = Folder.objects.create(name=directory.name,
                                           parent_folder=parent_folder,
                                           size=directory.size,
                                           created=directory.file_creation_time,
                                           is_top_folder=False if parent_folder else True,
                                           path=directory.path)
        if directory.includes:  # if directory contains book - save them
            cls._save_book_instances_to_db(new_folder, directory.includes)

        if directory.subdir:  # if directory contains subdirs - save them
            for subdir in directory.subdir:
                cls.save_structure_to_db(subdir, parent_folder=new_folder)
        return {'status': 200}

    @staticmethod
    def _save_book_instances_to_db(folder: Folder, books: list):
        for book in books:
            book_inst, is_created = Book.objects.get_or_create(title=book.name,
                                                               file_creation_time=book.file_creation_time,
                                                               extension=book.extension,
                                                               defaults={'size': book.size,
                                                                         'path': book.path,
                                                                         'rate': 1,
                                                                         'folder': folder,
                                                                         })
            if not is_created:
                book_inst.folder = folder
                book_inst.path = book.path
                book_inst.size = book.size
                book_inst.save()

    @staticmethod
    def clear_folders_structure():
        Folder.objects.all().delete()

    @classmethod
    def save_book_in_folder(cls, book: BookClass, folder: Folder) -> BookClass:
        book_inc = Book.objects.create(title=book.name, file_creation_time=book.file_creation_time,
                                       extension=book.extension, size=book.size, path=book.path,
                                       rate=1, folder=folder)
        return book_inc
