from rest_framework.reverse import reverse
from rest_framework import serializers
from ..models import Invoice, InvoiceItem

from apps.people.models import Supplier
from apps.product.models import Product

class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='document:invoice-detail',
        lookup_field='pk',
        )
    supplier_url = serializers.HyperlinkedRelatedField(
        view_name='people:supplier-detail',
        read_only=True,
    )
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())    

    supplier_name = serializers.SerializerMethodField(method_name='get_supplier_name')
    item_count = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = [
            'id','invoice_no','supplier_url','supplier',
            'supplier_name','date_of_issuance',
            'subtotal','taxes','total', 'url','item_count'
        ]

    def get_supplier_name(self, obj):
        return obj.supplier.company

    def get_item_count(self, obj):
        return obj.invoice_items.count()
    
class InvoiceItemSerializer(serializers.HyperlinkedModelSerializer):
    product_str = serializers.SerializerMethodField(method_name='get_product_str')
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())    
    invoice = serializers.PrimaryKeyRelatedField(queryset=Invoice.objects.all())    

    class Meta:
        model = InvoiceItem
        fields = [
            'id','invoice', 'product_str','product',
            'quantity', 'price',
            'item_subtotal','item_tax', 'item_total'
        ]

    def get_product_str(self, obj):
        return obj.product.__str__()