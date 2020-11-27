from django.test import TestCase

from book_finder.services.finder import Finder, Directory


class FinderTest(TestCase):
    path1 = 'D:\\Personal\\Books'
    path2 = 'D:\\Personal\\Books\\Math'

    def test_finder_path(self):
        finder = Finder()
        res = finder.find_books_in_system(self.path2)
        self.assertIsInstance(res, Directory)
