from rest_framework.viewsets import ModelViewSet
from .models import Leito
from .serializers import LeitoSerializer

class LeitoViewSet(ModelViewSet):
    queryset = Leito.objects.all()
    serializer_class = LeitoSerializer