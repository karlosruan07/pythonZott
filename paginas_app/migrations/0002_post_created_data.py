# Generated by Django 3.1.3 on 2021-01-23 19:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('paginas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]