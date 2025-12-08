from django.db import models

class Unidade(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    tipo_unidade = models.IntegerField()
    endereco = models.CharField(null=True, max_length=255)
    email = models.EmailField(null=True, max_length=255)
    telefone = models.CharField(null=True, max_length=15)

    class Meta:
        db_table = 'unidade_saude'

    def __str__(self):
        return self.nome
