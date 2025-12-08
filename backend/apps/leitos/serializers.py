from rest_framework import serializers
from .models import Leito

class LeitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leito
        fields = '__all__'