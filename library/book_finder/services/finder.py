from typing import Union, List
from dataclasses import dataclass, field
from functools import reduce
import os

from common.system_data import transform_unix_time


@dataclass
class BaseItem:
    name: str
    path: str  # file path
    size: float
    file_creation_time: str = None

    def __post_init__(self):
        self.file_creation_time = self._get_file_creation_time()

    def _get_file_creation_time(self):
        """Transform unix type time into common.
        Not a part of the public API
        """

        unix_time = os.path.getctime(self.path)
        return transform_unix_time(unix_time, False)


@dataclass
class Book(BaseItem):
    extension: str = None  # format: pdf, fb2, epub, etc


@dataclass
class Directory(BaseItem):
    includes: List[Book] = field(default_factory=list)  # contains books
    subdir: List['Directory'] = field(default_factory=list)  # contains subfolders

    def size_counter(self):
        self.size = reduce(lambda x, y: x + y.size, self.includes, self.includes[0].size)


class Finder:
    def find_books_in_system(self, path: str, dir_name: str = None) -> Union[Directory, dict]:
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
            directory = Directory(name=dir_name or path.split('\\')[0], path=path, includes=[], size=0)

            for item in item_to_scan:
                item_path = f'{path}\\{item}'
                *item_name_parts, item_extension = item.split('.')
                item_name = ''.join(item_name_parts)

                if os.path.isfile(item_path) and self._file_extension_checker(item_extension):
                    book = Book(name=item_name, path=item_path,
                                extension=item_extension, size=os.path.getsize(item_path) / 1000000)
                    directory.includes.append(book)

                elif os.path.isdir(item_path) and not item.startswith('.'):
                    directory.subdir.append(self.find_books_in_system(item_path, item))

                else:
                    continue
        directory.size_counter()
        return directory

    @staticmethod
    def _file_extension_checker(ext: str) -> bool:
        """Not a part of the public API"""
        extensions = '.pdf.fb2.txt.doc.docx.epub.djvu'
        return ext in extensions
