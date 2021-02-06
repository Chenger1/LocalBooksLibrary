from django.test import TestCase

from ebooks.models import Folder

import os
import shutil


class CheckFoldersUpdateTest(TestCase):

    def test_save_data_url_pattern(self):
        folder_path = 'D:\\Personal\\Books'
        resp = self.client.post('/save_data/', {'folder_path': folder_path}, follow=True)
        self.assertEqual(resp.status_code, 200, msg=resp.content)

    def test_view_url_exists_at_desired_location(self):
        self.test_save_data_url_pattern()
        resp = self.client.get('/check_folder_for_update/', follow=True)
        self.assertEqual(resp.status_code, 200, msg=resp.content)


class AddNewBookTest(TestCase):
    books_path = 'D:\\Projects\\TEST_FOLDER'
    folder_path = 'D:\\Projects\\TEST_FOLDER\\test'

    @classmethod
    def setUpTestData(cls):
        try:
            os.mkdir(cls.folder_path)
        except FileExistsError:
            os.rmdir(cls.folder_path)
            os.mkdir(cls.folder_path)
        cls.folder_inst = Folder.objects.create(name='Test_Folder',
                                                size=10, created='2020-10-10',
                                                path=cls.folder_path)

    @classmethod
    def tearDown(cls):
        files = os.scandir(cls.folder_path)
        for file in files:
            shutil.move(file.path, cls.books_path)
        os.rmdir(cls.folder_path)

    def test_post(self):
        folder = Folder.objects.get(pk=1)
        resp = self.client.post('/add_book_post/', {'folders': folder.pk,
                                                    'books': [f'{self.books_path}\\Django 3 By Example.pdf',
                                                              f'{self.books_path}\\KlassZadachiCompScienPyth.pdf']},
                                follow=True)
        self.assertEqual(resp.status_code, 200, msg=resp.content)


class UpdateInfoAboutBookTest(TestCase):
    folder_path = 'D:\\Personal\\Books'

    def test_get(self):
        self.client.post('/save_data/', {'folder_path': self.folder_path}, follow=True)
        resp = self.client.get('/update_info_about_books/', follow=True)
        self.assertEqual(resp.status_code, 200, msg=resp.content)
