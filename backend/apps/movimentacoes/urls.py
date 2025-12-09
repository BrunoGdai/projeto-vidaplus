from rest_framework.routers import DefaultRouter
from .views import ModelViewSet

router = DefaultRouter()
router.register(r'', ModelViewSet, basename='movimentacao')

urlpatterns = router.urls