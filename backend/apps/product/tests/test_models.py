from django.test import TestCase, Client
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from apps.product.models import (Category, SubCategory,
                                  Package, Tax, Product)
from apps.tools import constants


class CategoryModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(category_name='Category 1')

    def test_category_uniqueness(self):
        with self.assertRaises(Exception):
            Category.objects.create(category_name='Category 1')


class SubCategoryModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(category_name="Test Category")
        self.subcategory = SubCategory.objects.create(subcategory_name="Test Subcategory",
                                                      category=self.category)

    def test_subcategory_uniqueness(self):
        with self.assertRaises(IntegrityError):
            subcategory2 = SubCategory.objects.create(subcategory_name="Test Subcategory",
                                                      category=self.category)

    def test_subcategory_different_category_allowed(self):
        category2 = Category.objects.create(category_name="Test Category 2")
        subcategory2 = SubCategory.objects.create(subcategory_name="Test Subcategory",
                                                  category=category2)
        self.assertEqual(subcategory2.subcategory_name, "Test Subcategory")


class PackageModelTestCase(TestCase):
    def setUp(self):
        self.package = Package.objects.create(material=constants.OTHER,
                                              package_unit=constants.KILO,
                                              package_quantity=1.5)

    def test_create_package(self):
        self.assertEqual(str(self.package), f"{constants.OTHER}, 1.5kg")
        self.assertEqual(self.package.material, constants.OTHER)
        self.assertEqual(self.package.package_unit, constants.KILO)
        self.assertEqual(self.package.package_quantity, 1.5)

    def test_package_uniqueness(self):
        with self.assertRaises(IntegrityError):
            Package.objects.create(material=constants.OTHER,
                                   package_unit=constants.KILO,
                                   package_quantity=1.5)   


class TaxModelTestCase(TestCase):
    def test_tax_creation(self):
        tax = Tax.objects.create(value=24.0)
        self.assertEqual(str(tax), '24.0')

    def test_tax_creation_with_negative_value(self):
        try:
            Tax.objects.create(value=-5.0)
        except ValidationError as e:
            self.assertEqual(str(e), 'Tax value can not be negative')

    def test_tax_creation_with_invalid_type(self):
        with self.assertRaises(ValidationError):
            Tax.objects.create(value='invalid')

    def test_clean_method_with_negative_value(self):
        tax = Tax(value=-5.0)
        with self.assertRaises(ValidationError):
            tax.clean()

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(category_name='test category')
        self.subcategory = SubCategory.objects.create(subcategory_name="test subcategory",
                                                      category=self.category)
        self.package = Package.objects.create(material=constants.OTHER,
                                              package_unit=constants.KILO, package_quantity=1)
        self.tax_rate = Tax.objects.create(value=0.24)
        self.product = Product.objects.create(
            product_name="test product",
            subcategory=self.subcategory,
            package=self.package,
            tax_rate=self.tax_rate,
            summary="test summary",
            is_active=True,
            available=True,
            online_sell=True,
        )

    def test_product_creation(self):
        product_count = Product.objects.count()
        self.assertEqual(product_count, 1)

    def test_str_method(self):
        self.assertEqual(str(self.product), "test product - Other, 1kg")

    def test_unique_constraint(self):
        new_product = Product(
            product_name="test product", subcategory=self.subcategory,
            package=self.package
        )
        with self.assertRaises(Exception):
            new_product.save()

