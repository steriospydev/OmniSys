from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from apps.people.models import Supplier


class SupplierModelViewSetTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(self.user)
        self.supplier_data = {
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
        self.supplier= None
        

    def test_list_suppliers(self):
        self.supplier = Supplier.objects.create(**self.supplier_data)
        url = reverse('people:supplier-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['company'], 'Test Company')

    def test_retrieve_supplier(self):
        self.supplier = Supplier.objects.create(**self.supplier_data)

        url = reverse('people:supplier-detail', kwargs={'pk': self.supplier.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['company'], 'Test Company')

    def test_create_supplier(self):
        
        url = reverse('people:supplier-list')
        response = self.client.post(url, self.supplier_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supplier.objects.count(), 1)

    def test_update_supplier(self):
        self.supplier = Supplier.objects.create(**self.supplier_data)

        updated_data = {'company': 'Updated Company'}
        url = reverse('people:supplier-detail', kwargs={'pk': self.supplier.pk})
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Supplier.objects.get(pk=self.supplier.pk).company, 'Updated Company')

    def test_delete_supplier(self):
        self.supplier = Supplier.objects.create(**self.supplier_data)

        url = reverse('people:supplier-detail', kwargs={'pk': self.supplier.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Supplier.objects.count(), 0)
        