# Generated by Django 3.1.14 on 2023-05-10 18:00

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название места')),
                ('description_short', models.TextField(blank=True, verbose_name='Краткое описание')),
                ('description_long', tinymce.models.HTMLField(blank=True, verbose_name='Полное описание')),
                ('lng', models.FloatField(null=True, verbose_name='Долгота')),
                ('lat', models.FloatField(null=True, verbose_name='Широта')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(unique=True, upload_to='', verbose_name='Файл картинки')),
                ('number', models.IntegerField(default=0, verbose_name='Номер картинки')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place', verbose_name='Место')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
    ]
