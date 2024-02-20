from django.urls import path
from . import views

app_name='people'

urlpatterns = [
    path("supplier/", views.SupplierListCreateAPIView.as_view(),
          name="supplier"),
    path('supplier/<uuid:id>/',
         view=views.SupplierRetrieveUpdateDestroyAPIView.as_view(),
         name='supplier-actions'
)
]