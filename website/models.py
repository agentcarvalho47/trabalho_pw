from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )


