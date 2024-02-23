from django.test import TestCase
from apps.people.models import Supplier
from apps.people.api.serializers import SupplierSerializer

class SerializerTests(TestCase):
    def setUp(self):
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
        Supplier.objects.create(**self.supplier_data)
        self.supplier = Supplier.objects.first()

    def test_serialization(self):
        serializer = SupplierSerializer(instance=self.supplier)
        serialized_data = serializer.data
        expected_fields = set(['company', 'person', 'TIN_agency', 'TIN_num',
                               'city', 'area', 'address', 'zipcode', 'phone',
                               'email', 'id', 'sku_num'])
        self.assertEqual(set(serialized_data.keys()), expected_fields)

    def test_sku_num_generated(self):
        serializer = SupplierSerializer(instance=self.supplier)
        serialized_data = serializer.data
        self.assertIn('sku_num', serialized_data)
        self.assertTrue(serialized_data['sku_num'])

    def test_sku_num_has_2_chars(self):
        serializer = SupplierSerializer(instance=self.supplier)
        serialized_data = serializer.data
        self.assertEqual(len(serialized_data['sku_num']), 2)