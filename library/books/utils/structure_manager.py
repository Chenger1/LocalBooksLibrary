from typing import Tuple

from books.models import Folder


class StructureManager:
    """
        Stores information about opened folders.
        It uses when user tries to move though file system
        """

    structure = {}

    @classmethod
    def update_level(cls, folder_id: int, parent_folder_id: int = None):
        """
            If folder already in structure - pass
            If not, saves it and update parent folder ti include the id of this one
        """

        if not cls._check_item_in_structure(folder_id):
            cls.structure.update({
                folder_id: {
                    'parent_folder': parent_folder_id,
                    'next_folder': None
                }
            })
            try:
                cls._delete_old_next_folder(parent_folder_id)
                cls.structure[parent_folder_id]['next_folder'] = folder_id
            except KeyError:
                pass

    @classmethod
    def get_parent_folder(cls, current_folder_id: int) -> int:
        return cls.structure[current_folder_id].get('parent_folder', None)

    @classmethod
    def get_next_folder(cls, current_folder: int) -> int:
        return cls.structure[current_folder].get('next_folder', None)

    @classmethod
    def _check_item_in_structure(cls, item: int) -> bool:
        return item in cls.structure

    @classmethod
    def _delete_old_next_folder(cls, parent_id: int):
        try:
            old_next_folder = cls.structure[parent_id]['next_folder']
            cls.structure.pop(old_next_folder)
        except KeyError:
            pass

    @classmethod
    def get_folders(cls, current_folder_id: int) -> Tuple[int, None]:
        """
        :param current_folder_id:
        :return: ids of folders
        """

        return (cls.structure[current_folder_id].get('parent_folder', None),
                cls.structure[current_folder_id].get('next_folder', None))

    @classmethod
    def get_full_folder_nesting(cls, folder: Folder) -> list:
        nesting = [folder]
        if folder.is_top_folder:
            return nesting
        nesting.extend(cls.get_full_folder_nesting(folder.parent_folder))
        return nesting
