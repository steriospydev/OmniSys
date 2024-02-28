from decimal import Decimal
from django.urls import reverse
from rest_framework import status

from apps.tools.tests import BaseAPITestCase
from apps.product.models import Category, SubCategory, Tax, Package, Product


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

class PackageListCreateAPIViewTests(BaseAPITestCase):

    def test_list_packages(self):
        Package.objects.create(material='Paper', package_unit='kg', package_quantity=10.5)
        Package.objects.create(material='Glass', package_unit='Unit', package_quantity=100)

        token = self.perform_auth()
        url = reverse('product:package')
        response = self.client.get(url)
        expected_packages = ['Paper, 10.5kg', 'Glass, 100.0Unit']
        received_packages = [f"{package['material']}, {package['package_quantity']}{package['package_unit']}" for package in response.data]

        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}') 
        self.assertEqual(response.status_code, status.HTTP_200_OK)        
        self.assertCountEqual(expected_packages, received_packages)

    def test_create_package_success(self):
        token = self.perform_auth()
        url = reverse('product:package')
        data = {'material': 'Paper', 'package_unit': 'kg', 'package_quantity': '10.5'}
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Package.objects.count(), 1)
        self.assertEqual(str(Package.objects.get()), 'Paper, 10.5kg')

    def test_unique_constraints(self):
        token = self.perform_auth()
        Package.objects.create(material='Paper', package_unit='kg', package_quantity=10.5)
        url = reverse('product:package')
        data = {'material': 'Paper', 'package_unit': 'kg', 'package_quantity': '10.5'}
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Package.objects.count(), 1)
    
class ProductListCreateAPIViewTests(BaseAPITestCase):

    def setUp(self):
        super().setUp()
        self.category = Category.objects.create(category_name='Test Category')
        self.subcategory = SubCategory.objects.create(subcategory_name='Test Subcategory',
                                                      category=self.category)
        self.tax = Tax.objects.create(value=Decimal('10.00'))
        self.package = Package.objects.create(material='Paper', package_unit='kg', package_quantity=10.5)
        self.data = {
            'product_name': 'Test Product',
            'subcategory': str(self.subcategory.id),
            'package': str(self.package.id),
            'tax_rate': str(self.tax.id),
            'summary': 'Test Summary',
            'is_active': True,
            'available': False,
            'online_sell': False,
        }


    def test_create_product_success(self):
        token = self.perform_auth()
        url = reverse('product:products')
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        created_product = Product.objects.first()
        self.assertEqual(created_product.product_name, self.data['product_name'])
        self.assertEqual(created_product.subcategory, self.subcategory)  
        self.assertEqual(created_product.package, self.package)          
        self.assertEqual(created_product.tax_rate, self.tax)          
        self.assertEqual(created_product.summary, self.data['summary'])
        self.assertTrue(created_product.is_active)
        self.assertFalse(created_product.available)
        self.assertFalse(created_product.online_sell)

    def test_unique_constraints(self):
        token = self.perform_auth()     
        Product.objects.create(
            product_name=self.data['product_name'],
            subcategory=SubCategory.objects.first(),
            package=Package.objects.first(),
            tax_rate=Tax.objects.first(),
            summary=self.data['summary'],
            is_active=self.data['is_active'],
            available=self.data['available'],
            online_sell=self.data['online_sell']
        )

        url = reverse('product:products')
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 1)

    def test_list_products(self):
        token = self.perform_auth()
        url = reverse('product:products')
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assuming your API returns JSON data containing a list of products
        products = response.data
        self.assertEqual(len(products), Product.objects.count())



class CategoryRetrieveUpdateDestroyAPIViewTests(BaseAPITestCase):
    def setUp(self):
        super().setUp()
        self.category = Category.objects.create(category_name='Test Category')
        self.url_str = 'product:category-item'

    def test_retrieve_category(self):
        token = self.perform_auth()
        url = reverse(self.url_str, kwargs={'id': self.category.id})
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['category_name'], self.category.category_name)
        
    def test_update_category(self):
        token = self.perform_auth()
        url = reverse(self.url_str, kwargs={'id': self.category.id})
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        updated_data = {'category_name': 'Updated Category Name'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.category_name, updated_data['category_name'])

    def test_partial_update_category(self):
        token = self.perform_auth()
        url = reverse(self.url_str, kwargs={'id': self.category.id})
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        updated_data = {'category_name': 'Updated Category Name'}
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.category_name, updated_data['category_name'])

    def test_delete_category(self):
        token = self.perform_auth()
        url = reverse(self.url_str, kwargs={'id': self.category.id})
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Category.objects.filter(id=self.category.id).exists())

# class CategoryRetrieveUpdateDestroyAPIViewTests(BaseAPITestCase):
#     def setUp(self):
#         self.category = Category.objects.create(category_name='Test Category')
#         self.url_str =  'product:category-item'
#         self.token = self.perform_auth()

    
#     def test_retrieve_category(self):
#         token = self.perform_auth()
#         url = reverse(self.url_str, kwargs={'id': self.category.id})
#         self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, serializers.CategorySerializer(instance=self.category).data)

#     def test_update_category(self):
#         token = self.perform_auth()

#         url = reverse(self.url_str, kwargs={'id': self.category.id})
#         self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
#         updated_data = {'category_name': 'Updated Category Name'}
#         response = self.client.put(url, updated_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.category.refresh_from_db()
#         self.assertEqual(self.category.category_name, updated_data['category_name'])

#     # def test_partial_update_category(self):
#     #     url = reverse(self.url_str, kwargs={'id': self.category.id})
#     #     self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
#     #     updated_data = {'category_name': 'Updated Category Name'}
#     #     response = self.client.patch(url, updated_data, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_200_OK)
#     #     self.category.refresh_from_db()
#     #     self.assertEqual(self.category.category_name, updated_data['category_name'])

#     # def test_delete_category(self):
#     #     url = reverse(self.url_str, kwargs={'id': self.category.id})
#     #     self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
#     #     response = self.client.delete(url)
#     #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#     #     self.assertFalse(Category.objects.filter(id=self.category.id).exists())