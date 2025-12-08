from rest_framework import serializers
from .models import Suprimento

class SuprimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suprimento
        fields = '__all__'