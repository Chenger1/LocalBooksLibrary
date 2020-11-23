from django.test import TestCase

from book_finder.services.finder import find_books_in_system


class FinderTest(TestCase):
    path1 = 'D:\\Personal\\Books'
    path2 = 'D:\\Personal\\Books\\Math'

    def test_finder_path(self):
        res = find_books_in_system(self.path1)
        self.assertGreater(len(res['LocalLibraryBaseDir']['includes']), 1)
