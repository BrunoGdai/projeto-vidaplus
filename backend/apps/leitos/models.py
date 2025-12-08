from django.db import models

class Leito(models.Model):
    numero = models.CharField(max_length=255, unique=True)
    tipo = models.CharField(max_length=255, null=True)
    status = models.IntegerField()
    id_unidade = models.IntegerField()

    class Meta:
        db_table = 'leito'

    def __str__(self):
        return self.numero
