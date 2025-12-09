from rest_framework.routers import DefaultRouter
from .views import InternacaoViewSet

router = DefaultRouter()
router.register(r'', InternacaoViewSet, basename='internacao')

urlpatterns = router.urls