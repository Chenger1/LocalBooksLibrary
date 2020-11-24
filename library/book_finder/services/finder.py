from typing import Optional
import os


def find_books_in_system(path: str, dir_name: str = 'LocalLibraryBaseDir') -> Optional[dict]:
    """ Finds all the books for given path.
        :returns structure that includes folder and files like that:
        {
        'book_name': {'type': 'file',
                      'format': 'pdf',
                      'path': 'some/book_name.pdf'},
        'folder_name': {'type': 'folder',
                        'path': 'some/folder_name',
                        'includes': {dict, dict}
                        }
    }
        """
    structure = {
        dir_name: {
            'type': 'folder',
            'path': path,
            'includes': {}
        }
    }
    try:
        items_to_scan = os.listdir(path)
    except FileNotFoundError:
        return None
    else:

        for item in items_to_scan:
            item_path = f'{path}\\{item}'
            item_parts = item.split('.')
            item_name = '.'.join(item_parts[:-1])

            if os.path.isfile(item_path) and _file_extension_checker(item):
                structure[dir_name]['includes'].update(
                    {
                        item_name: {
                            'type': 'file',
                            'format': item_parts[-1],
                            'path': item_path,
                            'size': os.path.getsize(item_path) / 1000000
                            }
                    }
                )
            elif os.path.isdir(item_path) and not item.startswith('.'):
                dir_structure = find_books_in_system(item_path, item)
                structure[dir_name]['includes'].update(dir_structure)
            else:
                continue

    return structure


def _file_extension_checker(file: str) -> bool:
    """Not a part of the public API"""
    extension = '.pdf.fb2.txt.doc.docx.epub.djvu'
    return file.split('.')[-1] in extension
