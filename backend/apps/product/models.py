import uuid
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import pre_save

from apps.tools.models import TimeStamp
from apps.tools import signals
from apps.tools import constants

class Category(TimeStamp):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          db_index=True, editable=False)
    category_name = models.CharField("Category Name", unique=True,
                                      max_length=120)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['category_name']

    def __str__(self):
        return f'{self.category_name}'

    def get_num_products(self):
        subcategories = self.subs.all()
        return sum(subcategory.get_num_products() for subcategory in subcategories)

class SubCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          db_index=True, editable=False)
    subcategory_name = models.CharField("SubCategory Name", max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='subs')

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'
        ordering = ['subcategory_name']
        constraints = [
            models.UniqueConstraint(fields=['subcategory_name', 'category'],
                                    name='unique_category')]

    def __str__(self):
        return f'{self.subcategory_name}'

    def get_num_products(self):
        products = self.sub_products.all()
        return len(products)

class Package(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          db_index=True, editable=False)
    material = models.CharField("Material", max_length=10,
                                choices=constants.MATERIAL_CHOICES,
                                default=constants.OTHER)
    package_unit = models.CharField("Measure Unit", max_length=5,
                                    choices=constants.PACKAGE_UNITS_CHOICES,
                                    default=constants.OTHER)
    package_quantity = models.DecimalField("Quantity", default=00.00,
                                           max_digits=5, decimal_places=1)

    class Meta:
        verbose_name = 'Package'
        verbose_name_plural = 'Packages'
        constraints = [
            models.UniqueConstraint(fields=['material', 'package_unit',
                                            'package_quantity'],
                                    name='unique_package')
        ]

    def __str__(self):
        return f'{self.material}, {self.package_quantity}{self.package_unit} '

class Tax(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          db_index=True, editable=False)
    value = models.DecimalField('Value %',  default=00.00,
                                max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Tax'
        verbose_name_plural = 'Taxes'

    def __str__(self):
        return f'{self.value}'

    def clean(self):
        if self.value < 0:
            raise ValidationError('Tax value can not be negative')

class Product(TimeStamp):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          db_index=True, editable=False)
    product_name = models.CharField("Product Name", max_length=120)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,
                                    related_name='sub_products')
    package = models.ForeignKey(Package, on_delete=models.CASCADE,
                                related_name='package_products')
    tax_rate = models.ForeignKey(Tax, on_delete=models.CASCADE, null=True,
                                 blank=True)
    summary = models.TextField("Description", null=True, blank=True)
    sku_num = models.CharField(max_length=3, unique=True,
                               blank=True, null=True, editable=False)

    is_active = models.BooleanField('Active', default=True)
    available = models.BooleanField('Available', default=False)
    online_sell = models.BooleanField('Online', default=False)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['product_name']
        constraints = [
            models.UniqueConstraint(fields=['product_name', 'package'],
                                    name='unique_product')
        ]

    def __str__(self):
        return f'{self.product_name} - {self.package}'

pre_save.connect(lambda sender, instance, **kwargs:
                 signals.generate_sku_num(sender, instance, k=3),
                 sender=Product)