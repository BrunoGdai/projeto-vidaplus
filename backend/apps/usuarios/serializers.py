from rest_framework import serializers
from .models import Usuario

class SignupSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    senha = serializers.CharField(write_only=True)
    perfil_id = serializers.IntegerField()
    paciente_id = serializers.IntegerField(required=False, allow_null=True)
    profissional_id = serializers.IntegerField(required=False, allow_null=True)

    def create(self, validated_data):
        user = Usuario(
            username=validated_data["username"],
            email=validated_data["email"],
            perfil_id=validated_data["perfil_id"],
            paciente_id=validated_data.get("paciente_id"),
            profissional_id=validated_data.get("profissional_id")
        )
        user.set_password(validated_data["senha"])
        user.save(using="default")
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    senha = serializers.CharField()
