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

class IPS(models.Model):
    cedula = models.CharField(max_length=255, unique=True)
    nombreApellido = models.CharField(max_length=512)

    class Meta:
      verbose_name_plural = "ipss"

class SET(models.Model):
    cedula = models.CharField(max_length=255, unique=True)
    nombreApellido = models.CharField(max_length=512)

    class Meta:
      verbose_name_plural = "sets"

class SFP(models.Model):
    cedula = models.CharField(max_length=255, unique=True)
    nombreApellido = models.CharField(max_length=512)
    departamento = models.CharField(max_length=255,blank=True,null=True)
    distrito = models.CharField(max_length=255,blank=True,null=True)

    class Meta:
      verbose_name_plural = "sfps"

class MJ(models.Model):
    cedula = models.CharField(max_length=255, unique=True)
    nombreApellido = models.CharField(max_length=512)
    departamento = models.CharField(max_length=255,blank=True,null=True)
    distrito = models.CharField(max_length=255,blank=True,null=True)

    class Meta:
      verbose_name_plural = "mjs"

class Jubilado(models.Model):
    cedula = models.CharField(max_length=255, unique=True)
    nombreApellido = models.CharField(max_length=512)
    departamento = models.CharField(max_length=255,blank=True,null=True)
    distrito = models.CharField(max_length=255,blank=True,null=True)

    class Meta:
      verbose_name_plural = "jubilados"

class Tekopora(models.Model):
    cedula = models.CharField(max_length=255, unique=True)
    nombreApellido = models.CharField(max_length=512)
    departamento = models.CharField(max_length=255,blank=True,null=True)
    distrito = models.CharField(max_length=255,blank=True,null=True)

    class Meta:
      verbose_name_plural = "tekoporas"