from books.models import Folder, Author, Book

from book_finder.services.finder import Directory


class Saver:
    def save_structure_to_db(self, directory: Directory, parent_folder: Folder = None) -> dict:
        new_folder = Folder.objects.create(name=directory.name,
                                           parent_folder=parent_folder,
                                           size=directory.size,
                                           created=directory.file_creation_time,
                                           is_top_folder=False if parent_folder else True)
        if directory.includes:  # if directory contains book - save them
            self._save_book_instances_to_db(new_folder, directory.includes)

        if directory.subdir:  # if directory contains subdirs - save them
            for subdir in directory.subdir:
                self.save_structure_to_db(subdir, parent_folder=new_folder)

        return {'status': 'OK'}

    @staticmethod
    def _save_book_instances_to_db(parent_folder: Folder, books: list):
        for book in books:
            Book.objects.create(title=book.name, size=book.size,
                                path=book.path, file_creation_time=book.file_creation_time,
                                last_read_time=book.file_creation_time,
                                rate=1, folder=parent_folder, extension=book.extension)
