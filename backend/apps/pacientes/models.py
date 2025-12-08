from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    sexo = models.IntegerField()
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(null=True, max_length=255)
    id_unidade = models.IntegerField()

    class Meta:
        db_table = 'paciente'

    def __str__(self):
        return self.nome
