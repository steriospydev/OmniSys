from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet



from .serializers import InvoiceItemSerializer, InvoiceSerializer
from  ..models import InvoiceItem, Invoice

class InvoiceModelViewSet(ModelViewSet):    
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]


class InvoiceItemListAPIView(ListAPIView):
    serializer_class = InvoiceItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        invoice_id = self.kwargs.get('invoice_id')
        invoice = get_object_or_404(Invoice, id=invoice_id)
        return InvoiceItem.objects.filter(invoice=invoice)

class InvoiceItemDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer
    permission_classes = [IsAuthenticated]