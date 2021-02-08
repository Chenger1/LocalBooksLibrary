from django.test import TestCase


class ListBookViewTest(TestCase):
    def test_list_book_view(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200, msg=resp.content)
