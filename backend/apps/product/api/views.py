from . import serializers
from ..models import Category ,SubCategory, Tax, Package, Product

from apps.tools.views import (BaseListCreateAPIView,
                              BaseRetrieveUpdateDestroyAPIView)

class CategoryListCreateAPIView(BaseListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

class SubCategoryListCreateAPIView(BaseListCreateAPIView):
    queryset = SubCategory.objects.all()   
    serializer_class = serializers.SubCategorySerializer

class TaxListCreateAPIView(BaseListCreateAPIView):
    queryset = Tax.objects.all()   
    serializer_class = serializers.TaxSerializer

class PackageListCreateAPIView(BaseListCreateAPIView):
    queryset = Package.objects.all()   
    serializer_class = serializers.PackageSerializer

class ProductListCreateAPIView(BaseListCreateAPIView):
    queryset = Product.objects.all()   
    serializer_class = serializers.ProductSerializer

class CategoryRetrieveUpdateDestroyAPIView(
    BaseRetrieveUpdateDestroyAPIView
):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

class SubCategoryRetrieveUpdateDestroyAPIView(
    BaseRetrieveUpdateDestroyAPIView
):
    queryset = SubCategory.objects.all()
    serializer_class = serializers.SubCategorySerializer

class TaxRetrieveUpdateDestroyAPIView(
    BaseRetrieveUpdateDestroyAPIView
):
    queryset = Tax.objects.all()
    serializer_class = serializers.TaxSerializer

class PackageRetrieveUpdateDestroyAPIView(
    BaseRetrieveUpdateDestroyAPIView
):
    queryset = Package.objects.all()
    serializer_class = serializers.PackageSerializer

class ProductRetrieveUpdateDestroyAPIView(
    BaseRetrieveUpdateDestroyAPIView
):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer