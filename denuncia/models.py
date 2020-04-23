from django.db import models
from django.utils import timezone


class Denuncia(models.Model):
    cedula = models.CharField(max_length=8, verbose_name=u"Cedula de Identidad", help_text=u"Favor introduzca su número de cedula", default='0',null=False, blank=False)
    nombreApellido=models.CharField(max_length=512, verbose_name=u"Nombres y Apellidos", help_text=u"Favor introduzca sus nombres y apellidos", default='Nombres Apellidos', null=False, blank=False)
    celular = models.CharField(max_length=15, verbose_name=u"Celular", help_text=u"Favor introduzca número de celular sin + o código de país", default='0', null=False, blank=False)
    denunciaTexto = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.cedula
        
    class Meta:
        verbose_name_plural = "Denuncias"
