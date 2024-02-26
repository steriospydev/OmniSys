from django.urls import reverse
from rest_framework import serializers

from ..models import Category, SubCategory, Tax, Package, Product

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product:category-item',
        lookup_field='id',
        )    
    
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'url']

class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product:sub-item',
        lookup_field='id',
        )
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category_url = serializers.SerializerMethodField(method_name='get_category_url')
    
    class Meta:
        model = SubCategory
        fields = ['id', 'subcategory_name', 'category', 'category_url', 'url']

    def get_category_url(self, obj):
        request = self.context.get('request')
        category_id = obj.category.id
        if request is not None:
            return request.build_absolute_uri(reverse('product:category-item', args=[category_id]))
        return None
    
class TaxSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product:tax-item',
        lookup_field='id',
        )
    class Meta:
        model = Tax
        fields = ['id', 'value', 'url']

    def validate_value(self, value):
        if value < 0:
            raise serializers.ValidationError("Tax value cannot be negative.")
        return value
    
class PackageSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product:package-item',
        lookup_field='id',
        )
    class Meta:
        model = Package
        fields = ['id', 'package_unit', 'material', 'package_quantity', 'url']



class ProductSerializer(serializers.HyperlinkedModelSerializer):
    subcategory = serializers.PrimaryKeyRelatedField(queryset=SubCategory.objects.all())
    package = serializers.PrimaryKeyRelatedField(queryset=Package.objects.all())
    tax_rate = serializers.PrimaryKeyRelatedField(queryset=Tax.objects.all())
    url = serializers.HyperlinkedIdentityField(
        view_name='product:product-item',
        lookup_field='id'
    )
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'subcategory', 'package',
                  'tax_rate', 'summary', 'sku_num', 'is_active', 
                  'available', 'online_sell', 'url']
 