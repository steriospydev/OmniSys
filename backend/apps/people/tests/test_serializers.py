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

    def test_serialization(self):
        supplier = Supplier.objects.create(**self.supplier_data)
        serializer = SupplierSerializer(instance=supplier)
        serialized_data = serializer.data

        # Check if all fields are present in the serialized data
        expected_fields = set(['company', 'person', 'TIN_agency', 'TIN_num',
                               'city', 'area', 'address', 'zipcode', 'phone',
                               'email', 'id'])
        self.assertEqual(set(serialized_data.keys()), expected_fields)

        # Add more specific checks for each field if needed

    def test_deserialization(self):
        serializer = SupplierSerializer(data=self.supplier_data)
        self.assertTrue(serializer.is_valid())
        supplier = serializer.save()

        # Ensure the deserialized Supplier object matches the expected data
        self.assertEqual(supplier.company, self.supplier_data['company'])
        self.assertEqual(supplier.person, self.supplier_data['person'])
        # Add assertions for other fields

    

    # Add more tests for required fields validation if needed
