from django.test import TestCase

import os

from books.services.system_services import init_system_data_file, write_data_to_file, check_books_folder_last_update


class SystemTest(TestCase):
    def test_init_system_data_file(self):
        file = init_system_data_file()
        self.assertEquals(os.path.isfile(file), True)

    def test_check_books_folder_last_update(self):
        file = init_system_data_file()

        data_to_write = {'folder_path': 'D:\\Personal\\Books',
                         'last_time_update': '2020-11-28'}
        write_data_to_file(data_to_write, file)
        result = check_books_folder_last_update(file)
        self.assertEquals(result, False)
