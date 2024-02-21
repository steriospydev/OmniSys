# tests/test_models.py
from django.test import TestCase
from apps.people.models import Supplier

class ModelTests(TestCase):
    def test_supplier_creation(self):
        supplier = Supplier.objects.create(
            company='Test Company',
            person='Test Person',
            TIN_agency='Test Agency',
            TIN_num='123456789',
            city='Test City',
            area='Test Area',
            address='Test Address',
            zipcode='12345',
            phone='1234567890',
            email='test@test.com'
        )
        self.assertEqual(Supplier.objects.count(), 1)

    def test_unique_TIN_num(self):
        supplier1 = Supplier.objects.create(
            company='Test Company 1',
            person='Test Person 1',
            TIN_agency='Test Agency 1',
            TIN_num='123456789',
            city='Test City 1',
            area='Test Area 1',
            address='Test Address 1',
            zipcode='12345',
            phone='1234567890',
            email='test1@test.com'
        )
        # Attempt to create another supplier with the same TIN_num
        with self.assertRaises(Exception) as context:
            supplier2 = Supplier.objects.create(
                company='Test Company 2',
                person='Test Person 2',
                TIN_agency='Test Agency 2',
                TIN_num='123456789',  # Same TIN_num as supplier1
                city='Test City 2',
                area='Test Area 2',
                address='Test Address 2',
                zipcode='12345',
                phone='1234567890',
                email='test2@test.com'
            )
        self.assertTrue('UNIQUE constraint failed' in str(context.exception))

    def test_unique_company(self):
        supplier1 = Supplier.objects.create(
            company='Test Company 1',
            person='Test Person 1',
            TIN_agency='Test Agency 1',
            TIN_num='123456780',  # Different TIN_num
            city='Test City 1',
            area='Test Area 1',
            address='Test Address 1',
            zipcode='12345',
            phone='1234567890',
            email='test1@test.com'
        )
        # Attempt to create another supplier with the same company name
        with self.assertRaises(Exception) as context:
            supplier2 = Supplier.objects.create(
                company='Test Company 1',  # Same company name as supplier1
                person='Test Person 2',
                TIN_agency='Test Agency 2',
                TIN_num='123456781',  # Different TIN_num
                city='Test City 2',
                area='Test Area 2',
                address='Test Address 2',
                zipcode='12345',
                phone='1234567890',
                email='test2@test.com'
            )
        self.assertTrue('UNIQUE constraint failed' in str(context.exception))

    def test_create_with_minimum_fields(self):
        # Create a Supplier with only company name and TIN number
        supplier = Supplier.objects.create(
            company='Test Company',
            TIN_num='123456789'
        )

        # Retrieve the created Supplier from the database
        saved_supplier = Supplier.objects.get(id=supplier.id)

        # Check if the saved Supplier matches the provided data
        self.assertEqual(saved_supplier.company, 'Test Company')
        self.assertEqual(saved_supplier.TIN_num, '123456789')

        # Ensure other fields are set to their default values or are null
        self.assertIsNone(saved_supplier.person)
        self.assertIsNone(saved_supplier.TIN_agency)