from ..models import Supplier
from .serializers import SupplierSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


class SupplierModelViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]
    queryset = Supplier.objects.all()
    
