from ebooks.models import Folder, Ebook, Extension

from books.services.get_book import get_book_instance_by_title
from books.services.save_to_db import Saver as sv
from books.models import Book

from book_finder.services.finder import Directory
from book_finder.services.finder import Book as BookClass


class Saver:

    @classmethod
    def save_structure_to_db(cls, directory: Directory, parent_folder: Folder = None) -> dict:
        new_folder = cls.save_folder_in_db(directory, parent_folder)

        if directory.includes:  # if directory contains book - save them
            cls._save_book_instances_to_db(new_folder, directory.includes)

        if directory.subdir:  # if directory contains subdirs - save them
            for subdir in directory.subdir:
                cls.save_structure_to_db(subdir, parent_folder=new_folder)
        return {'status': 200}

    @classmethod
    def _save_book_instances_to_db(cls, folder: Folder, books: list):
        for book in books:
            base_book_inst = cls._get_base_book(book.name, book)
            book_inst, is_created = Ebook.objects.get_or_create(base_book=base_book_inst,
                                                                file_creation_time=book.file_creation_time,
                                                                extension=cls._save_extension_to_db(book.extension.lower()),
                                                                defaults={'size': book.size,
                                                                          'path': book.path,
                                                                          'folder': folder,
                                                                          'base_book': base_book_inst})
            if not is_created:
                book_inst.folder = folder
                book_inst.path = book.path
                book_inst.size = book.size
                book_inst.save()

    @staticmethod
    def clear_folders_structure():
        Folder.objects.all().delete()

    @classmethod
    def save_book_in_folder(cls, book: BookClass, folder: Folder) -> Ebook:
        base_book_inst = cls._get_base_book(book.name, book)
        book_inc = Ebook.objects.create(file_creation_time=book.file_creation_time,
                                        extension=cls._save_extension_to_db(book.extension.lower()),
                                        size=book.size, path=book.path,
                                        folder=folder, base_book=base_book_inst)
        return book_inc

    @staticmethod
    def save_folder_in_db(directory: Directory, parent_folder: Folder = None) -> Folder:
        new_folder = Folder.objects.create(name=directory.name,
                                           parent_folder=parent_folder,
                                           size=directory.size,
                                           created=directory.file_creation_time,
                                           is_top_folder=False if parent_folder else True,
                                           path=directory.path)
        return new_folder

    @staticmethod
    def _get_base_book(title: str, book: BookClass) -> Book:
        base_book_inst = get_book_instance_by_title(title)
        if not base_book_inst:  # If there is no any books with specific title we create one
            base_book_inst = sv.save_book_to_db(book.to_dict())
        return base_book_inst

    @staticmethod
    def _save_extension_to_db(ext_name: str) -> Extension:
        ext, _ = Extension.objects.get_or_create(name=ext_name)
        return ext
