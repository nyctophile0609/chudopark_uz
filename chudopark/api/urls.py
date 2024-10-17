from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Schema view for Swagger and Redoc
schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Router setup
router = DefaultRouter()
router.register(r'users', UserModelViewSet, basename='users')
router.register(r'categories', CategoryModelViewSet, basename='categories')
router.register(r'products', ProductModelViewSet, basename='products')
router.register(r'product-subsets', ProductSubsetModelViewSet, basename='product-sets')
router.register(r'applications', ApplicationModelViewSet, basename='applications')
router.register(r'discounts', DiscountModelViewSet, basename='discounts')

# URL patterns
urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
]