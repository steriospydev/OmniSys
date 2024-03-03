from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'product'

router = routers.DefaultRouter()

router.register('product', views.ProductModelViewSet)
router.register('category', views.CategoryModelViewSet)
router.register('subcategory', views.SubCategoryModelViewSet)
router.register('package', views.PackageModelViewSet)
router.register('tax', views.TaxModelViewSet)


urlpatterns = [ path('', include(router.urls)),]
