import uuid
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.signals import pre_save, pre_delete, post_delete
from django.dispatch import receiver


from apps.tools.models import TimeStamp
from apps.people.models import Supplier
from apps.product.models import Product

# Create your models here.
class Invoice(TimeStamp):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            db_index=True, editable=False)  
    invoice_no = models.BigIntegerField('Invoice No')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date_of_issuance = models.DateTimeField('Issue Date')

    subtotal = models.DecimalField('Subtotal', max_digits=12,
                                    decimal_places=2, blank=True, default=0)
    taxes = models.DecimalField('Tax', max_digits=12, decimal_places=2,
                                 blank=True, default=0)
    total = models.DecimalField('Total', max_digits=12, decimal_places=2,
                                 blank=True, default=0)

    class Meta:
        ordering = ('-created_at',)
        unique_together = ('invoice_no', 'supplier')    
    
    def __str__(self) -> str:
        return f'{self.supplier} - {self.invoice_no}'
    
    @property
    def get_total_taxes(self):
        return sum([item.get_item_tax for item in self.invoice_items.all()])
        

    @property
    def get_subtotal(self):
        return sum([item.get_item_subtotal for item in self.invoice_items.all()])
     
    @property
    def get_total(self):
        return self.get_subtotal + self.get_total_taxes


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.taxes = self.get_total_taxes
        self.subtotal = self.get_subtotal
        self.total = self.get_total
        super().save(*args, **kwargs)
                     
class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='invoice_items',
                                on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_items',
                                on_delete=models.CASCADE)
    quantity = models.DecimalField('Quantity', default=00.00,
                                   max_digits=5, decimal_places=1,
                                   validators=[MinValueValidator(0)])
    price  = models.DecimalField(max_digits=10, decimal_places=2,
                                 default=00.00, blank=True,
                                 validators=[MinValueValidator(0)])    
   
    item_subtotal = models.DecimalField('Subtotal',max_digits=10, decimal_places=2,
                                default=00.00, blank=True,
                                validators=[MinValueValidator(0)])
    item_tax = models.DecimalField('Taxes', default=00.00,
                              blank=True, max_digits=4,
                              decimal_places=1,
                              validators=[MinValueValidator(0)])
    item_total = models.DecimalField('Total',max_digits=10, decimal_places=2,
                                default=00.00, blank=True,
                                validators=[MinValueValidator(0)])
    
    def __str__(self) -> str:
        return f'{self.product.product_name}'
    
    @property
    def get_item_subtotal(self):
        return self.quantity * self.price
    
    @property
    def get_item_tax(self):
        return self.get_item_subtotal * (self.product.tax_rate.value /Decimal('100'))
    
    @property
    def get_item_total(self):
        return self.get_item_subtotal + self.get_item_tax
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.item_subtotal = self.get_item_subtotal
        self.item_tax = self.get_item_tax
        self.item_total = self.get_item_total
        super().save(*args, **kwargs)


    
@receiver(pre_save, sender=InvoiceItem)
@receiver(pre_delete, sender=InvoiceItem)
@receiver(post_delete, sender=InvoiceItem)
def update_order_totals(sender, instance, **kwargs):
    invoice = instance.invoice
    # Update the totals for the order
    invoice.taxes = invoice.get_total_taxes
    invoice.subtotal = invoice.get_subtotal
    invoice.total = invoice.get_total
    invoice.save()