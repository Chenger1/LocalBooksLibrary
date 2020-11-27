from typing import Optional, List
from dataclasses import dataclass, field
import os


@dataclass
class BaseItem:
    name: str
    path: str  # file path
    size: float


@dataclass
class Book(BaseItem):
    extension: str  # format: pdf, fb2, epub, etc


@dataclass
class Folder(BaseItem):
    includes: List[Book] = field(default_factory=list)  # contains books
    subfolders: List['Folder'] = field(default_factory=list)  # contains subfolders


class Finder:
    def find_books_in_system(self, path: str, dir_name: str = 'LocalLibraryBaseDir') -> Optional[Folder]:
        """ Finds all the books for given path.
        :return None if path is wrong.
        :return Folder instance
        """

        try:
            item_to_scan = os.listdir(path)
        except FileNotFoundError:
            return None
        else:
            folder = Folder(name=dir_name, path='', includes=[], size=0)

            for item in item_to_scan:
                item_path = f'{path}\\{item}'
                *item_name, item_extension = item.split('.')

                if os.path.isfile(item_path) and self._file_extension_checker(item_extension):
                    book = Book(name=item_name, path=item_path,
                                extension=item_extension, size=os.path.getsize(item_path) / 1000000)
                    folder.includes.append(book)
                elif os.path.isdir(item_path) and not item.startswith('.'):
                    folder.subfolders.append(self.find_books_in_system(item_path, item))
                else:
                    continue

        return folder

    @staticmethod
    def _file_extension_checker(ext: str) -> bool:
        """Not a part of the public API"""
        extensions = '.pdf.fb2.txt.doc.docx.epub.djvu'
        return ext in extensions
