from django.test import TestCase


class CheckFoldersUpdateTest(TestCase):

    def test_save_data_url_pattern(self):
        folder_path = 'D://Personal/Books'
        resp = self.client.post('/save_data/', {'folder_path': folder_path}, follow=True)
        self.assertEqual(resp.status_code, 200, msg=resp.content)

    def test_view_url_exists_at_desired_location(self):
        self.test_save_data_url_pattern()
        resp = self.client.get('/check_folder_for_update/', follow=True)
        self.assertEqual(resp.status_code, 200, msg=resp.content)

