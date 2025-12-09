from rest_framework.viewsets import ModelViewSet
from .models import Movimentacao
from .serializers import MovimentacaoSerializer

class MovimentacaoViewSet(ModelViewSet):
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer