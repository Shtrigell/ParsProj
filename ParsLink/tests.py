from django.test import TestCase


class TestParsLink(TestCase):

    def test_index(self):
        response = self.client.get('//')
        self.assertEqual(response.status_code, 200)

    def test_history(self):
        response = self.client.get('/history/')
        self.assertEqual(response.status_code, 200)

