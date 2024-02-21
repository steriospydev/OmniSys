from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.people.models import Supplier
from apps.people.api.serializers import SupplierSerializer

class SupplierListCreateAPIViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_login(self.user) 
        self.url = reverse('people:supplier')
        self.data = {
            'company': 'Test Company',
            'person': 'Test Person',
            'TIN_agency': 'Test Agency',
            'TIN_num': '123456789',
            'city': 'Test City',
            'area': 'Test Area',
            'address': 'Test Address',
            'zipcode': '12345',
            'phone': '1234567890',
            'email': 'test@test.com'
        }

    def test_create_supplier(self):       
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supplier.objects.count(), 1)
        self.assertEqual(Supplier.objects.get().company, 'Test Company')

    def test_list_suppliers(self):
        Supplier.objects.create(company='Test Company', TIN_num='123456789')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
       
class SupplierRetrieveUpdateDestroyAPIViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_login(self.user)  # Authenticate the client
        self.supplier = Supplier.objects.create(
            company='Test Company',
            TIN_num='123456789',
            person='Test Person',
            city='Test City',
            area='Test Area',
            address='Test Address',
            zipcode='12345',
            phone='1234567890',
            email='test@test.com'
        )

        self.url = reverse('people:supplier-actions', kwargs={'id': self.supplier.id})

    def test_retrieve_supplier(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['company'], 'Test Company')

    def test_update_supplier(self):
        data = {'company': 'Updated Company'}
        response = self.client.patch(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Supplier.objects.get(id=self.supplier.id).company, 'Updated Company')

    def test_delete_supplier(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Supplier.objects.count(), 0)
