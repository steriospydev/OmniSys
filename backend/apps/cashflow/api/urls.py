from django.urls import path, include
from rest_framework import routers
from . import views

app_name='cashflow'
router = routers.DefaultRouter()
router.register('payeelabel', views.PayeeLabelModelViewSet)
router.register('payee', views.PayeeModelViewSet)
router.register('payment', views.PaymentModelViewSet)
router.register('source', views.SourceModelViewSet)
router.register('income', views.IncomeModelViewSet)


urlpatterns = [ path('', include(router.urls)),]
