# Generated by Django 3.1.3 on 2021-02-23 00:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('paginas_app', '0004_auto_20210222_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 23, 0, 4, 31, 983117, tzinfo=utc)),
        ),
    ]
