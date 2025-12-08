from django.db import models

class Internacao(models.Model):
    descricao = models.CharField(max_length=255)
    data_hora_entrada = models.DateTimeField()
    data_hora_saida = models.DateTimeField(null=True)
    id_paciente = models.IntegerField()
    id_profissional = models.IntegerField()
    id_leito = models.IntegerField()

    class Meta:
        db_table = 'internacao'

    def __str__(self):
        return self.descricao