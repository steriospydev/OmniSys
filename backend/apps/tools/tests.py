from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

class BaseAPITestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='testuser', password='12345')

    def perform_auth(self, username='testuser', password='12345'):
        url = reverse('rest_login')
        data = {'username': username, 'password': password}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data['key']
