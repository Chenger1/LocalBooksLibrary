from django.test import TestCase

from book_finder.services.finder import Finder

from ebooks.services.save_data_to_db import Saver


class SaverTest(TestCase):
    path = 'D:\\Personal\\Books'

    @classmethod
    def setUpTestData(cls):
        finder = Finder()
        cls.folder = finder.find_books_in_system(cls.path)

    def test_saver(self):
        saver = Saver()
        status = saver.save_structure_to_db(self.folder)
        self.assertEquals(status['status'], 200)
