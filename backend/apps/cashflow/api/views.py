from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from ..models import (PayeeLabel, Payee, Payment,
                      Source, Income)
from . import serializers

class PayeeLabelModelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PayeeLabelSerializer
    permission_classes = [IsAuthenticated]
    queryset = PayeeLabel.objects.all()

class PayeeModelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PayeeSerializer
    permission_classes = [IsAuthenticated]
    queryset = Payee.objects.all()
    
class PaymentModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  
    serializer_class = serializers.PaymentSerializer
    queryset = Payment.objects.all()

class SourceModelViewSet(viewsets.ModelViewSet):    
    serializer_class = serializers.SourceSerializer
    permission_classes = [IsAuthenticated]
    queryset = Source.objects.all()

class IncomeModelViewSet(viewsets.ModelViewSet):    
    serializer_class = serializers.IncomeSerializer
    permission_classes = [IsAuthenticated]
    queryset = Income.objects.all()
