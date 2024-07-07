from .views import ProductViewSet
from rest_framework.routers import DefaultRouter # type: ignore

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
urlpatterns = router.urls