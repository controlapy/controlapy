# Generated by Django 3.0.5 on 2020-04-23 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('denuncia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='denuncia',
            name='celular',
            field=models.CharField(default='0', help_text='Favor introuzca número de celular sin + o código de país', max_length=15, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='denuncia',
            name='cedula',
            field=models.CharField(default='0', help_text='Favor introuzca su número de cedula', max_length=8, verbose_name='Cedula de Identidad'),
        ),
        migrations.AlterField(
            model_name='denuncia',
            name='nombreApellido',
            field=models.CharField(default='Nombres Apellidos', help_text='Favor introuzca sus nombres y apellidos', max_length=512, verbose_name='Nombres y Apellidos'),
        ),
    ]