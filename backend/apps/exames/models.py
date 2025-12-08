from django.db import models

class Exame(models.Model):
    tipo_exame = models.CharField(max_length=255)
    data_agendamento = models.DateField()
    data_hora_realizacao = models.DateTimeField()
    resultado = models.CharField()
    descricao = models.CharField(max_length=255)
    id_paciente = models.IntegerField()
    id_profissional = models.IntegerField()

    class Meta:
        db_table = 'exame'

    def __str__(self):
        return self.descricao