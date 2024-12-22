from django.test import TestCase, Client


class PostCreateTest(TestCase):
    def setUp(self):
        self.client = Client()
        