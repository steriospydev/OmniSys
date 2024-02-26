from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
      path("products/",
            views.ProductListCreateAPIView.as_view(),
            name="products"),   
      path("category/",
            views.CategoryListCreateAPIView.as_view(),
            name="category"),      
      path("sub/",
            views.SubCategoryListCreateAPIView.as_view(),
            name="sub"),
      path("package/",
            views.PackageListCreateAPIView.as_view(),
            name="package"),
      path("tax/",
            views.TaxListCreateAPIView.as_view(),
            name="tax"),
      path("products/<uuid:id>/",
            views.ProductRetrieveUpdateDestroyAPIView.as_view(),
            name="product-item"),  
      path('category/<uuid:id>/',
            view=views.CategoryRetrieveUpdateDestroyAPIView.as_view(),
            name='category-item'),
      path('sub/<uuid:id>/',
            view=views.SubCategoryRetrieveUpdateDestroyAPIView.as_view(),
            name='sub-item'),     
      path('package/<uuid:id>/',
            view=views.PackageRetrieveUpdateDestroyAPIView.as_view(),
            name='package-item'), 
      path('tax/<uuid:id>/',
            view=views.TaxRetrieveUpdateDestroyAPIView.as_view(),
            name='tax-item'),      
]