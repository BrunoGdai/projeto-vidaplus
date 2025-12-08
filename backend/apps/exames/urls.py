from rest_framework.routers import DefaultRouter
from .views import ExameViewSet

router = DefaultRouter()
router.register(r'', ExameViewSet, basename='exame')

urlpatterns = router.urls