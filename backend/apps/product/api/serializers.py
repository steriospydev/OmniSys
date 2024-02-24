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
    category_url = serializers.HyperlinkedIdentityField(
        view_name='product:category-item',
        lookup_field='id',
        read_only=True
    )
    class Meta:
        model = SubCategory
        fields = ['id', 'subcategory_name', 'category', 'category_url', 'url']