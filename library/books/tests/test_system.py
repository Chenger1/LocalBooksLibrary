from django.test import TestCase

import os

from books.services.system_services import init_system_data_file, write_data_to_file, check_books_folder_last_update


class SystemTest(TestCase):
    file_path = None

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.file_path)

    def test_init_system_data_file(self):
        file = init_system_data_file()
        self.assertEquals(os.path.isfile(file), True)

    def test_check_books_folder_last_update(self):
        SystemTest.file_path = init_system_data_file()

        data_to_write = {'folder_path': 'D:\\Personal\\Books',
                         'last_time_update': '2020-11-28 14:33:55'}
        write_data_to_file(data_to_write, self.file_path)
        result = check_books_folder_last_update(self.file_path)
        self.assertEquals(result, False)
