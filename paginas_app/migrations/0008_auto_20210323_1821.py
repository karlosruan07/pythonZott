# Generated by Django 3.1.4 on 2021-03-23 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('paginas_app', '0007_login_sistema'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('nota', models.DecimalField(decimal_places=1, max_digits=2)),
                ('descricao', models.TextField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='auth.user'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Prova',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('arquivo', models.FileField(upload_to='')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='paginas_app.materia')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='paginas_app.post')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='materia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='paginas_app.materia'),
            preserve_default=False,
        ),
    ]
