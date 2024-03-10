# tests/test_models.py
from django.test import TestCase
from apps.people.models import Supplier

class ModelTests(TestCase):
    def setUp(self):
        self.create_supplier = Supplier.objects.create(
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
        self.supplier = Supplier.objects.first()

    def test_supplier_creation(self):        
        self.assertEqual(Supplier.objects.count(), 1)

    def test_sku_generated(self):
        self.assertIsNotNone(self.supplier.sku_num)

    def test_unique_company_and_TIN_num(self):
        with self.assertRaises(Exception) as context_company:
            with self.assertRaises(Exception) as context_TIN:
                Supplier.objects.create(
                    company='Test Company',  # Same company name 
                    TIN_num='123456783',     # Same TIN_num 
                )
                # Check failure of TIN_num
                self.assertTrue('UNIQUE constraint failed TIN_num' in str(context_TIN.exception))
            # Check failure of company
            self.assertTrue('UNIQUE constraint failed company' in str(context_company.exception))
           
    def test_create_with_minimum_fields(self):
        new_supplier = Supplier.objects.create(
            company='Test Company 2',
            TIN_num='0123456789'
        )
        saved_supplier = Supplier.objects.get(id=new_supplier.id)       
        # Check if the saved Supplier matches the provided data
        self.assertEqual(saved_supplier.company, 'Test Company 2')
        self.assertEqual(saved_supplier.TIN_num, '0123456789')
        self.assertIsNotNone(saved_supplier.sku_num)

    def test_phone_has_10_digits(self):
        supplier = Supplier.objects.first()
        self.assertEqual(len(supplier.phone), 10)

    def test_TIN_num_has_9_digits(self):
        supplier = Supplier.objects.first()
        tin_num = supplier.TIN_num
        self.assertTrue(tin_num.isdigit())
        self.assertEqual(len(tin_num), 9)

    def test_email_has_correct_format(self):
        supplier = Supplier.objects.first()
        email = supplier.email
        self.assertTrue('@' in email and '.' in email)

    def test_sku_length(self):
        self.assertEqual(len(self.supplier.sku_num), 2)
    
    def test_str_method(self):
        self.assertEqual(str(self.supplier), 'Test Company')