from rest_framework.routers import DefaultRouter
from .views import LeitoViewSet

router = DefaultRouter()
router.register(r'', LeitoViewSet, basename='leito')

urlpatterns = router.urls