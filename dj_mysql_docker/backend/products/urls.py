from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# Create a router and register the viewset with it
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')

# Define URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Includes all the URLs from the router
]
