from rest_framework.viewsets import ModelViewSet
from .models import Suprimento
from .serializers import SuprimentoSerializer

class SuprimentoViewSet(ModelViewSet):
    queryset = Suprimento.objects.all()
    serializer_class = SuprimentoSerializer