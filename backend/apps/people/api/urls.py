from django.urls import path, include
from rest_framework import routers
from . import views

app_name='people'

router = routers.DefaultRouter()

router.register('supplier', views.SupplierModelViewSet)

urlpatterns = [ path('', include(router.urls)),]



