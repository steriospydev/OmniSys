from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
# from rest_framework_simplejwt import views as jwt_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="OmniSys API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="steriospydev@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('auth/', include('dj_rest_auth.urls')),
   # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
   # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
   path('people/', include('apps.people.api.urls')),
   path('product/', include('apps.product.api.urls')),
   path('cashflow/', include('apps.cashflow.api.urls')),

   path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
]