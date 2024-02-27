from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from django.contrib.auth.models import User
from apps.product.models import Category, SubCategory, Tax, Package, Product
from decimal import Decimal

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



class CategoryListCreateAPIViewTest(BaseAPITestCase):
    def test_list_categories(self):
        Category.objects.create(category_name='Category 1')
        Category.objects.create(category_name='Category 2')

        token = self.perform_auth()
        url = reverse('product:category')
        response = self.client.get(url)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_categories = ['Category 1', 'Category 2']
        received_categories = [category['category_name'] for category in response.data]
        self.assertCountEqual(expected_categories, received_categories)

    def test_create_category_success(self):
        token = self.perform_auth()
        url = reverse('product:category')
        data = {'category_name': 'Test Category'}
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().category_name, 'Test Category')

    def test_create_category_validation_error(self):
        token = self.perform_auth()
        url = reverse('product:category')
        existing_category = Category.objects.create(category_name='Existing Category')
        data = {'category_name': 'Existing Category'}
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Category.objects.count(), 1)  # No new category should be created

    

class SubCategoryListCreateAPIViewTest(BaseAPITestCase):
    def test_list_subcategories(self):
        category = Category.objects.create(category_name='Test Category')
        SubCategory.objects.create(subcategory_name='Subcategory 1', category=category)
        SubCategory.objects.create(subcategory_name='Subcategory 2', category=category)                

        token = self.perform_auth()
        url = reverse('product:sub')
        response = self.client.get(url)
        expected_subcategories = ['Subcategory 1', 'Subcategory 2']
        received_subcategories = [subcategory['subcategory_name'] for subcategory in response.data]

        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}') 
        self.assertEqual(response.status_code, status.HTTP_200_OK)        
        self.assertCountEqual(expected_subcategories, received_subcategories)

    def test_create_subcategory_success(self):
        token = self.perform_auth()
        category = Category.objects.create(category_name='Test Category')
        url = reverse('product:sub')
        data = {'subcategory_name': 'Test Subcategory', 'category': category.id}
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SubCategory.objects.count(), 1)
        self.assertEqual(SubCategory.objects.get().subcategory_name, 'Test Subcategory')

    def test_create_subcategory_same_name_in_same_category_validation_error(self):
        token = self.perform_auth()
        category = Category.objects.create(category_name='Test Category')
        SubCategory.objects.create(subcategory_name='Existing Subcategory', category=category)
        url = reverse('product:sub')
        data = {'subcategory_name': 'Existing Subcategory', 'category': category.id}
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(SubCategory.objects.count(), 1)  

    def test_create_subcategory_same_name_in_different_categories(self):
        token = self.perform_auth()
        category1 = Category.objects.create(category_name='Category 1')
        category2 = Category.objects.create(category_name='Category 2')
        url = reverse('product:sub')
        data1 = {'subcategory_name': 'Shared Subcategory', 'category': category1.id}
        data2 = {'subcategory_name': 'Shared Subcategory', 'category': category2.id}
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response1 = self.client.post(url, data1, format='json')
        response2 = self.client.post(url, data2, format='json')
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SubCategory.objects.count(), 2)


class TaxCategoryListCreateAPIViewTest(BaseAPITestCase):
    def test_list_tax_categories(self):
        Tax.objects.create(value=Decimal('10.00'))
        Tax.objects.create(value=Decimal('20.00'))

        token = self.perform_auth()
        url = reverse('product:tax')
        response = self.client.get(url)
        expected_values = ['10.00', '20.00']
        received_values = [str(tax['value']) for tax in response.data]

        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}') 
        self.assertEqual(response.status_code, status.HTTP_200_OK)        
        self.assertCountEqual(expected_values, received_values)

    def test_create_tax_category_success(self):
        token = self.perform_auth()
        url = reverse('product:tax')
        data = {'value': '30.00'}
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tax.objects.count(), 1)
        self.assertEqual(Tax.objects.get().value, Decimal('30.00'))

    def test_create_tax_category_same_value_error(self):
        token = self.perform_auth()
        Tax.objects.create(value=Decimal('40.00'))
        url = reverse('product:tax')
        data = {'value': '40.00'}
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Tax.objects.count(), 1)  

    def test_create_tax_category_negative_value_error(self):
        token = self.perform_auth()
        url = reverse('product:tax')
        data = {'value': '-10.00'}
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Tax.objects.count(), 0)

    def test_create_tax_category_data_type_decimal(self):
        token = self.perform_auth()
        url = reverse('product:tax')
        data = {'value': '10.50'}
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tax.objects.count(), 1)
        self.assertIsInstance(Tax.objects.get().value, Decimal)