from django.db import models

class Suprimento(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    tipo = models.CharField(max_length=255)
    quantidade_atual = models.IntegerField()
    quantidade_minima = models.IntegerField()
    id_unidade = models.IntegerField()

    class Meta:
        db_table = 'suprimento'

    def __str__(self):
        return self.nome
