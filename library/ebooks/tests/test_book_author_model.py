from django.test import TestCase

from ebooks.models import Folder


class FolderTest(TestCase):

    def test_folder_create(self):
        folder = Folder.objects.create(name='First', size=9.5, created='2020-11-25')
        self.assertEquals(folder.name, 'First')

    def test_subfolder_create(self):
        main_parent_folder = Folder.objects.create(name='LocalLibraryBaseDir', size=1, created='2020-11-25')
        folder = Folder.objects.create(name='Main', size=1, created='2020-11-25', parent_folder=main_parent_folder)
        subfolder1 = Folder.objects.create(name='First', size=9.5, created='2020-11-25', parent_folder=folder)
        subfolder2 = Folder.objects.create(name='Second', size=1.5, created='2020-11-25', parent_folder=folder)

        self.assertEquals(len(folder.subfolders.all()), 2)
        self.assertEquals(subfolder2.parent_folder.name, 'Main')
