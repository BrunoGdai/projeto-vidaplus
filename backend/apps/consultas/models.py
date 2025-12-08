from django.db import models

class Consulta(models.Model):
    data_hora = models.DateTimeField()
    status = models.IntegerField()
    id_paciente = models.IntegerField()
    id_profissional = models.IntegerField()

    class Meta:
        db_table = 'consulta'

    def __str__(self):
        return self.tipo_movimentacao + " " + str(self.data_hora)
