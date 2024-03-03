from django.contrib import admin
from .models import Invoice, InvoiceItem


class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    fields = [
        'product', 'quantity', 'price',
        'item_tax', 'item_subtotal', 'item_total'
    ]


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['supplier', 'invoice_no',
                    'date_of_issuance', 'subtotal',
                    'total', 'taxes']
    inlines = [InvoiceItemInline]
