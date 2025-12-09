from rest_framework.viewsets import ModelViewSet
from .models import Internacao
from .serializers import InternacaoSerializer

class InternacaoViewSet(ModelViewSet):
    queryset = Internacao.objects.all()
    serializer_class = InternacaoSerializer