from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Usuario
from .serializers import SignupSerializer, LoginSerializer
from .auth import gerar_token

class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = gerar_token(user)
            return Response({"token": token}, status=201)
        return Response(serializer.errors, status=400)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        username = serializer.validated_data["username"]
        senha = serializer.validated_data["senha"]

        try:
            usuario = Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            return Response({"erro": "Usuário não encontrado"}, status=404)

        if not usuario.check_password(senha):
            return Response({"erro": "Senha incorreta"}, status=401)

        token = gerar_token(usuario)
        return Response({"token": token})
