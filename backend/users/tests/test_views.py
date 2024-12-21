from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse
from users.models import Member

class SignUpTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('signup')

    def test_sign_up(self):
        response = self.client.post(self.url, {'first_name': 'Test',
                                               'last_name': 'User',
                                               'username': 'TestUser',
                                               'email': 'TestUser@TestUser.com',
                                               'password': 'TestPassword'})
        self.assertEqual(response.status_code, 302)


class SignInTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('signin')

    def test_sign_in(self):
        user = Member.objects.create_user(username = 'TestUser',
                                          password = 'TestPassword',)        
        response = self.client.post(self.url, {'username': 'TestUser',
                                               'password': 'TestPassword'})
        self.assertEqual(response.status_code, 302)


class SignOutTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('signout')
        self.user = Member.objects.create_user(username = 'TestUser',
                                               password = 'TestPassword',)   

    def test_sign_out(self):    
        self.client.login(username='TestUser', 
                          password='TestPassword')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)


class ProfileEditTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('edit')
        self.user = Member.objects.create_user(username = 'TestUser',
                                               password = 'TestPassword',)  
        
    def test_profile_edit(self):
        self.client.login(username='TestUser',
                          password='TestPassword')
        response = self.client.post(self.url, {'bio': 'Test Bio',
                                               'upload': SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpg"),
                                               'date_of_birth': '2021-01-01',})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/profile/')
        