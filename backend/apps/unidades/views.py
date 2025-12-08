from rest_framework.viewsets import ModelViewSet
from .models import Unidade
from .serializers import UnidadeSerializer

class UnidadeViewSet(ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer