from django.db import models

class Perfil(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'perfil'
        managed = False

    def __str__(self):
        return self.nome

class Permissao(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=100, unique=True)
    descricao = models.CharField(max_length=255)

    class Meta:
        db_table = 'permissao'
        managed = False

class PerfilPermissao(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, db_column='perfil_id')
    permissao = models.ForeignKey(Permissao, on_delete=models.CASCADE, db_column='permissao_id')

    class Meta:
        db_table = 'perfil_permissao'
        managed = False
        unique_together = ('perfil', 'permissao')
