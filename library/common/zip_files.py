import zipfile
import os


class ZipManager:
    @classmethod
    def extract_zip_files(cls, dir_path: str):
        item_to_scan = os.listdir(dir_path)
        for item in item_to_scan:
            item_path = f'{dir_path}\\{item}'
            if os.path.isfile(item_path) and item[-3:] == 'zip':
                # Do not use is_zipfile because it returns True for "fb2", "epub"
                # So I manually check for "zip" extension
                cls._extracting_zip_files_by_given_path(item_path, dir_path)
                cls._delete_zip_file(item_path)
            elif os.path.isdir(item_path) and not item.startswith('.'):
                cls.extract_zip_files(item_path)
            else:
                continue

    @staticmethod
    def _extracting_zip_files_by_given_path(zip_file: str, dir_path: str):
        with zipfile.ZipFile(zip_file) as zip_file:
            zip_file.extractall(dir_path)

    @staticmethod
    def _delete_zip_file(zip_file: str):
        os.remove(zip_file)
