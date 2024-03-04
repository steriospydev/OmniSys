from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'document'

router = routers.DefaultRouter()

router.register('invoice', views.InvoiceModelViewSet)
urlpatterns = [ 
    path('', include(router.urls)),
    path('invoice/<uuid:invoice_id>/items/',
          views.InvoiceItemListAPIView.as_view(),
          name='invoice-item-list'),
    path('invoice/items/<int:pk>/', 
         views.InvoiceItemDetailAPIView.as_view(),
           name='invoice-item-detail'),
    ]