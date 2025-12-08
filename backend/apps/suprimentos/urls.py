from rest_framework.routers import DefaultRouter
from .views import SuprimentoViewSet

router = DefaultRouter()
router.register(r'', SuprimentoViewSet, basename='suprimento')

urlpatterns = router.urls