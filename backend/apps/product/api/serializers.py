from django.urls import reverse
from rest_framework import serializers

from ..models import Category, SubCategory, Tax, Package, Product

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product:category-detail',
        lookup_field='pk',
        )    
    count_products = serializers.SerializerMethodField(method_name='get_count_products')

    def get_count_products(self, obj):
        return obj.get_num_products
    
    class Meta:
        model = Category
        fields = ['id', 'category_name','count_products','url']

class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product:subcategory-detail',
        lookup_field='pk',
        )
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())    
    count_products = serializers.SerializerMethodField(method_name='get_count_products')
    category_name = serializers.SerializerMethodField(method_name='get_category_name')
   
    def get_count_products(self, obj):
        return obj.get_num_products
    
    def get_category_name(self, obj):
        return obj.category.category_name
    
    class Meta:
        model = SubCategory
        fields = ['id', 'subcategory_name', 'category',
                  'category_name', 'count_products', 'url']

    
class TaxSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product:tax-detail',
        lookup_field='pk',
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
        view_name='product:package-detail',
        lookup_field='pk',
        )
    count_products = serializers.SerializerMethodField(method_name='get_count_products')

    class Meta:
        model = Package
        fields = ['id', 'package_unit', 'material',
                  'package_quantity', 'count_products',
                  'url']

    def get_count_products(self, obj):
        return obj.get_num_products
    
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    subcategory = serializers.PrimaryKeyRelatedField(queryset=SubCategory.objects.all())
    package = serializers.PrimaryKeyRelatedField(queryset=Package.objects.all())
    tax_rate = serializers.PrimaryKeyRelatedField(queryset=Tax.objects.all())
    url = serializers.HyperlinkedIdentityField(
        view_name='product:product-detail',
        lookup_field='pk'
    )

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'subcategory', 'package',
                  'tax_rate', 'summary', 'sku_num', 'is_active', 
                  'available', 'online_sell', 'url']
 