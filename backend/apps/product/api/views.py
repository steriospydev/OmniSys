from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated

from .serializers import (CategorySerializer,
                          SubCategorySerializer)
from ..models import Category ,SubCategory


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