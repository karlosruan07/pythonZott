# Generated by Django 3.1.4 on 2021-04-12 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas_app', '0009_auto_20210330_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prova',
            name='post',
        ),
        migrations.AlterField(
            model_name='prova',
            name='arquivo',
            field=models.FileField(upload_to='pdf/'),
        ),
    ]