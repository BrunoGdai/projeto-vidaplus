from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Perfil(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    descricao = models.TextField(null=True)

    class Meta:
        managed = False
        db_table = 'perfil'

    def __str__(self):
        return self.nome


class Permissao(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True)

    class Meta:
        managed = False
        db_table = 'permissao'


class PerfilPermissao(models.Model):
    id = models.BigAutoField(primary_key=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    permissao = models.ForeignKey(Permissao, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'perfil_permissao'
        unique_together = ('perfil', 'permissao')


class Usuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    senha = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    ativo = models.BooleanField(default=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.RESTRICT)

    # FK opcionais
    paciente_id = models.BigIntegerField(null=True)
    profissional_id = models.BigIntegerField(null=True)

    class Meta:
        managed = False
        db_table = 'usuario'

    # Métodos utilitários
    def set_password(self, raw):
        self.senha = make_password(raw)

    def check_password(self, raw):
        return check_password(raw, self.senha)

    def __str__(self):
        return self.username
