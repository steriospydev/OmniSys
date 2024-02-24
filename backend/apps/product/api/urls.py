from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path("category/", views.CategoryListCreateAPIView.as_view(),
          name="category"),
    path('category/<uuid:id>/',
         view=views.CategoryRetrieveUpdateDestroyAPIView.as_view(),
         name='category-item'),

    path("category/sub/", views.SubCategoryListCreateAPIView.as_view(),
          name="sub"),
    path('category/sub/<uuid:id>/',
         view=views.SubCategoryRetrieveUpdateDestroyAPIView.as_view(),
         name='sub-item'),
]