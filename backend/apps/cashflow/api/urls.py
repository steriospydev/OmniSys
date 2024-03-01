from django.urls import path
from . import views

app_name='cashflow'

urlpatterns = [
    path('payeelabel/',
         views.PayeeLabelListCreateAPIView.as_view(),
         name='payeelabel'),
    path('payee/',
         views.PayeeListCreateAPIView.as_view(),
         name='payee'),
    path('payment/',
         views.PaymentListCreateAPIView.as_view(),
         name='payment'),
    path('source/',
         views.SourceListCreateAPIView.as_view(),
         name='source'),
    path('income/',
         views.IncomeListCreateAPIView.as_view(),
         name='income'),

    path('payeelabel/<uuid:id>/',
         views.PayeeLabelRetrieveUpdateDestroyAPIView.as_view(),
         name='payeelabel-item'),
    path('payee/<uuid:id>/',
         views.PayeeRetrieveUpdateDestroyAPIView.as_view(),
         name='payee-item'),
    path('payment/<uuid:id>/',
         views.PaymentRetrieveUpdateDestroyAPIView.as_view(),
         name='payment-item'),
    path('source/<uuid:id>/',
         views.SourceRetrieveUpdateDestroyAPIView.as_view(),
         name='source-item'),
    path('income/<uuid:id>/',
         views.IncomeRetrieveUpdateDestroyAPIView.as_view(),
         name='income-item'),
]