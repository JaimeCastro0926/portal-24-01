# Generated by Django 4.1.4 on 2023-01-18 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionDocente', '0017_alter_llamado_lista_estudiante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico',
            name='Evidencias',
            field=models.ImageField(blank=True, null=True, upload_to='historico/'),
        ),
    ]
