from django.test import TestCase


class CheckFoldersUpdateTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/check_folder_for_update/')
        self.assertEqual(resp.status_code, 200, msg=resp.content)
