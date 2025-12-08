from django.db import models

class Movimentacao(models.Model):
    tipo_movimentacao = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    data_hora = models.DateTimeField()
    id_suprimento = models.IntegerField()
    id_profissional = models.IntegerField()

    class Meta:
        db_table = 'movimentacao'

    def __str__(self):
        return self.tipo_movimentacao + " " + str(self.data_hora)
