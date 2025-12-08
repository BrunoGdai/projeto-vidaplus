from rest_framework.viewsets import ModelViewSet
from .models import Profissional
from .serializers import ProfissionalSerializer

class ProfissionalViewSet(ModelViewSet):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer