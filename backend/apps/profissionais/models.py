from django.db import models

class Profissional(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    tipo_profissional = models.IntegerField()
    especialidade = models.IntegerField()
    registro = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    id_unidade = models.IntegerField()

    class Meta:
        db_table = 'profissional'

    def __str__(self):
        return self.nome
