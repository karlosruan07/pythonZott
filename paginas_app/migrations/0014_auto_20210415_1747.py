# Generated by Django 3.1.4 on 2021-04-15 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas_app', '0013_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='cpf',
            field=models.CharField(max_length=11, null=True, verbose_name='CPF'),
        ),
    ]
