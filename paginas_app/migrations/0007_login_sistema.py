# Generated by Django 3.1.4 on 2021-03-06 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas_app', '0006_auto_20210222_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login_sistema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('password', models.TextField()),
            ],
        ),
    ]