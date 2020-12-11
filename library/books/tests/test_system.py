from django.test import TestCase

import os

from books.services.system_services import init_system_data_file


class SystemTest(TestCase):
    def test_init_system_data_file(self):
        file = init_system_data_file()
        self.assertEquals(os.path.isfile(file), True)
