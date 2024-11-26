# Generated by Django 4.2.16 on 2024-11-26 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CopiaImpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('superficie', models.CharField(max_length=40)),
                ('tamanio', models.IntegerField()),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fotolibro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamanio', models.IntegerField()),
                ('cant_hojas', models.IntegerField()),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SesionFotografica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=100)),
                ('activo', models.BooleanField()),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
