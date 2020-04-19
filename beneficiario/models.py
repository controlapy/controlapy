from django.db import models
from django.utils import timezone


class Beneficiario(models.Model):
    cedula = models.CharField(max_length=255, unique=True)

    class Meta:
      verbose_name_plural = "beneficiarios"

class Nangareko(models.Model):
    cedula = models.CharField(max_length=255, unique=True)
    nombreApellido = models.CharField(max_length=512)
    departamento = models.CharField(max_length=255,blank=True,null=True)
    distrito = models.CharField(max_length=255,blank=True,null=True)

    class Meta:
      verbose_name_plural = "nangarekos"

class Pytyvo(models.Model):
    cedula = models.CharField(max_length=255, unique=True)
    nombreApellido = models.CharField(max_length=512)
    departamento = models.CharField(max_length=255,blank=True,null=True)
    distrito = models.CharField(max_length=255,blank=True,null=True)

    class Meta:
      verbose_name_plural = "pytyvos"
