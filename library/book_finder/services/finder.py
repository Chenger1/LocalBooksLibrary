from typing import Union, List, Tuple
from dataclasses import dataclass, field, asdict
from functools import reduce
import os
import datetime

from common.system_data import transform_unix_time
from common.zip_files import ZipManager


@dataclass
class BaseItem:
    name: str
    path: str  # file path
    size: float
    file_creation_time: datetime = None

    def __post_init__(self):
        self.file_creation_time = self._get_file_creation_time()

    def _get_file_creation_time(self) -> datetime:
        """Transform unix type time into common.
        Not a part of the public API
        """

        unix_time = os.path.getctime(self.path)
        return transform_unix_time(unix_time)

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Book(BaseItem):
    extension: str = None  # format: pdf, fb2, epub, etc


@dataclass
class Directory(BaseItem):
    includes: List[Book] = field(default_factory=list)  # contains books
    subdir: List['Directory'] = field(default_factory=list)  # contains subfolders

    def size_counter(self):
        self.size = 0
        for arg in [self.includes, self.subdir]:
            if arg:
                self.size += reduce(lambda x, y: x + y.size, arg, arg[0].size)


class Finder:
    @classmethod
    def find_books_in_system(cls, path: str, dir_name: str = None) -> Union[Directory, dict]:
        """ Finds all the books for given path.
        :return None if path is wrong.
        :return Folder instance
        """
        if os.path.isfile(path):
            return {'status': 'Wrong path'}

        try:
            item_to_scan = os.listdir(path)
        except FileNotFoundError:
            return {'status': 'Wrong path'}
        else:
            directory = Directory(name=dir_name or path.split('\\')[-1], path=path, includes=[], size=0)

            for item in item_to_scan:
                item_path, item_extension, item_name = cls.slice_item_for_name_and_ext(item, path)

                if os.path.isfile(item_path) and cls._file_extension_checker(item_extension):
                    book = Book(name=item_name, path=item_path,
                                extension=item_extension, size=os.path.getsize(item_path) / 1000000)
                    directory.includes.append(book)

                elif os.path.isdir(item_path) and not item.startswith('.'):
                    directory.subdir.append(cls.find_books_in_system(item_path, item))

                else:
                    continue
        directory.size_counter()
        return directory

    @staticmethod
    def slice_item_for_name_and_ext(item_string: str, directory_path: str) -> Tuple[str, str, str]:
        item_path = f'{directory_path}\\{item_string}'
        *item_name_parts, item_extension = item_string.split('.')
        item_name = ''.join(item_name_parts)
        return item_path, item_extension, item_name

    @staticmethod
    def _file_extension_checker(ext: str) -> bool:
        """Not a part of the public API"""
        extensions = '.pdf.fb2.txt.doc.docx.epub.djvu'
        return ext.lower() in extensions

    @classmethod
    def create_book_instance(cls, book_path: str) -> Book:
        *item_name_parts, item_extension = book_path.split('.')
        item_name_parts = ''.join(item_name_parts)
        item_name = ''.join(item_name_parts.split('\\')[-1])
        book = Book(name=item_name, path=book_path,
                    extension=item_extension, size=os.path.getsize(book_path) / 1000000)
        return book
