# Generated by Django 5.0.1 on 2024-02-05 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_rename_nombre_usuario_usuario_nombre_completo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='confirmar_contraseña',
            field=models.CharField(default=False, max_length=255),
        ),
        migrations.AddField(
            model_name='usuario',
            name='contraseña',
            field=models.CharField(default=True, max_length=255),
        ),
    ]
