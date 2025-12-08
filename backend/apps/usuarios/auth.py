import datetime
import jwt
from django.conf import settings

def gerar_token(usuario):
    payload = {
        "user_id": usuario.id,
        "username": usuario.username,
        "perfil_id": usuario.perfil_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=4),
        "iat": datetime.datetime.utcnow(),
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
