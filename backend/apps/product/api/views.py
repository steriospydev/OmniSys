from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated

from .serializers import (CategorySerializer, SubCategorySerializer,
                          TaxSerializer, PackageSerializer,
                          ProductSerializer)
from ..models import Category ,SubCategory, Tax, Package, Product


class CategoryListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

class CategoryRetrieveUpdateDestroyAPIView(
    RetrieveUpdateDestroyAPIView
):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

class SubCategoryListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SubCategory.objects.all()   
    serializer_class = SubCategorySerializer
    lookup_field = 'id'

class SubCategoryRetrieveUpdateDestroyAPIView(
    RetrieveUpdateDestroyAPIView
):
    permission_classes = [IsAuthenticated]
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    lookup_field = 'id'

class TaxListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Tax.objects.all()   
    serializer_class = TaxSerializer
    lookup_field = 'id'

class TaxRetrieveUpdateDestroyAPIView(
    RetrieveUpdateDestroyAPIView
):
    permission_classes = [IsAuthenticated]
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer
    lookup_field = 'id'

class PackageListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Package.objects.all()   
    serializer_class = PackageSerializer
    lookup_field = 'id'

class PackageRetrieveUpdateDestroyAPIView(
    RetrieveUpdateDestroyAPIView
):
    permission_classes = [IsAuthenticated]
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    lookup_field = 'id'


class ProductListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()   
    serializer_class = ProductSerializer
    lookup_field = 'id'

class ProductRetrieveUpdateDestroyAPIView(
    RetrieveUpdateDestroyAPIView
):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'