# Generated by Django 3.1.3 on 2021-02-23 00:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('paginas_app', '0003_auto_20210123_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 23, 0, 2, 13, 517322, tzinfo=utc)),
        ),
    ]
