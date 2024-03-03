from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from . import serializers
from ..models import Category ,SubCategory, Tax, Package, Product


class CategoryModelViewSet(ModelViewSet):    
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticated]

class SubCategoryModelViewSet(ModelViewSet):
    queryset = SubCategory.objects.all()   
    serializer_class = serializers.SubCategorySerializer
    permission_classes = [IsAuthenticated]

class TaxModelViewSet(ModelViewSet):
    queryset = Tax.objects.all()   
    serializer_class = serializers.TaxSerializer
    permission_classes = [IsAuthenticated]

class PackageModelViewSet(ModelViewSet):
    queryset = Package.objects.all()   
    serializer_class = serializers.PackageSerializer
    permission_classes = [IsAuthenticated]

class ProductModelViewSet(ModelViewSet):    
    queryset = Product.objects.all()   
    serializer_class = serializers.ProductSerializer
    permission_classes = [IsAuthenticated]
