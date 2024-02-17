from django.contrib.auth.models import User

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

class SignupAPITestCase(APITestCase):
    def setUp(self):
        self.existing_user = User.objects.create_user(username='existinguser',
                                                      password='testpassword')
        
    def test_signup_success(self):
        url = reverse('account:signup')  
        data = {'username': 'testuser', 'password': 'testpassword'} 
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_signup_failure(self):
        url = reverse('account:signup')  
        data = {}  
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_failure_user_exists(self):
        url = reverse('account:signup')  
        data = {'username': 'existinguser', 'password': 'testpassword'}  # Trying to sign up with an existing username
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class LoginAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.first()

    def test_token_created(self):
        self.assertTrue(Token.objects.filter(user=self.user).exists())

    def test_login_success(self):
        url = reverse('account:login')  # Assuming 'account:login' is the URL name for LoginAPIView
        data = {'username': 'testuser', 'password': 'testpassword'}  # Correct login credentials
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Token', response.data['data'])  # Check if Token is returned in response data

    def test_login_failure_incorrect_password(self):
        url = reverse('account:login')  # Assuming 'account:login' is the URL name for LoginAPIView
        data = {'username': 'testuser', 'password': 'wrongpassword'}  # Incorrect password
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_failure_invalid_user(self):
        url = reverse('account:login')  # Assuming 'account:login' is the URL name for LoginAPIView
        data = {'username': 'invaliduser', 'password': 'testpassword'}  # Non-existing user
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_failure_missing_data(self):
        url = reverse('account:login')  
        data = {}  
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data['data'])
        self.assertIn('password', response.data['data'])

    def test_token_generation_on_signup(self):
        url = reverse('account:signup') 
        data = {'username': 'newuser', 'password': 'newpassword'}  
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        new_user = User.objects.get(username='newuser')
        self.assertTrue(Token.objects.filter(user=new_user).exists())

    def test_token_retrieval_on_login(self):
        url = reverse('account:login')  
        data = {'username': 'testuser', 'password': 'testpassword'}  
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Token', response.data['data'])
        self.assertEqual(response.data['data']['Token'], self.token.key)