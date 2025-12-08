from rest_framework.routers import DefaultRouter
from .views import ProfissionalViewSet

router = DefaultRouter()
router.register(r'', ProfissionalViewSet, basename='profissional')

urlpatterns = router.urls