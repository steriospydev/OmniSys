from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated

from ..models import Supplier
from .serializers import SupplierSerializer

class SupplierListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    lookup_field = 'id'

class SupplierRetrieveUpdateDestroyAPIView(
    RetrieveUpdateDestroyAPIView
):
    permission_classes = [IsAuthenticated]
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    lookup_field = 'id'