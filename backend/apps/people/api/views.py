from ..models import Supplier
from .serializers import SupplierSerializer
from apps.tools.views import (BaseListCreateAPIView,
                              BaseRetrieveUpdateDestroyAPIView)

class SupplierListCreateAPIView(BaseListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierRetrieveUpdateDestroyAPIView(
    BaseRetrieveUpdateDestroyAPIView
):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer