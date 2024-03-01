from apps.tools.views import (BaseListCreateAPIView,
                              BaseRetrieveUpdateDestroyAPIView)
from ..models import (PayeeLabel, Payee, Payment,
                      Source, Income)

from . import serializers

class PayeeLabelListCreateAPIView(BaseListCreateAPIView):
    queryset = PayeeLabel.objects.all()
    serializer_class = serializers.PayeeLabelSerializer

class PayeeListCreateAPIView(BaseListCreateAPIView):
    queryset = Payee.objects.all()
    serializer_class = serializers.PayeeSerializer

class PaymentListCreateAPIView(BaseListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = serializers.PaymentSerializer

class SourceListCreateAPIView(BaseListCreateAPIView):
    queryset = Source.objects.all()
    serializer_class = serializers.SourceSerializer

class IncomeListCreateAPIView(BaseListCreateAPIView):
    queryset = Income.objects.all()
    serializer_class = serializers.IncomeSerializer

class PayeeLabelRetrieveUpdateDestroyAPIView(
    BaseRetrieveUpdateDestroyAPIView
):
    queryset = PayeeLabel.objects.all()
    serializer_class = serializers.PayeeLabelSerializer

class PayeeRetrieveUpdateDestroyAPIView(
    BaseRetrieveUpdateDestroyAPIView
):
    queryset = Payee.objects.all()
    serializer_class = serializers.PayeeSerializer

class PaymentRetrieveUpdateDestroyAPIView(
    BaseRetrieveUpdateDestroyAPIView
):
    queryset = Payment.objects.all()
    serializer_class = serializers.PaymentSerializer

class SourceRetrieveUpdateDestroyAPIView(
    BaseRetrieveUpdateDestroyAPIView
):
    queryset = Source.objects.all()
    serializer_class = serializers.SourceSerializer

class IncomeRetrieveUpdateDestroyAPIView(
    BaseRetrieveUpdateDestroyAPIView
):
    queryset = Income.objects.all()
    serializer_class = serializers.IncomeSerializer