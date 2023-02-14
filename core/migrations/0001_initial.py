# Generated by Django 4.1.7 on 2023-02-14 16:39

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('name', models.CharField(max_length=100, verbose_name='Название группы')),
            ],
            options={
                'verbose_name': 'Группа работ',
                'verbose_name_plural': 'Группы работ',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('name_ru', models.CharField(max_length=250, verbose_name='Название проекта (рус.)')),
                ('name', models.CharField(blank=True, max_length=250, verbose_name='Название проекта (англ.)')),
                ('description_ru', models.TextField(blank=True, max_length=5000, verbose_name='Описание полное (рус.)')),
                ('description', models.TextField(blank=True, max_length=5000, verbose_name='Описание (англ.)')),
                ('description_short_ru', models.TextField(blank=True, max_length=2500, verbose_name='Описание полное (рус.)')),
                ('description_short', models.TextField(blank=True, max_length=2500, verbose_name='Описание (англ.)')),
                ('link', models.URLField(blank=True, verbose_name='Ссылка на проект')),
                ('git', models.URLField(blank=True, verbose_name='Ссылка на гит')),
                ('path', models.CharField(blank=True, max_length=200, verbose_name='Папка проекта')),
                ('isActive', models.BooleanField(default=True, verbose_name='Активен?')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.group', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='ProjectImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.BooleanField(default=False, verbose_name='Главное изображение?')),
                ('alt', models.CharField(blank=True, max_length=500, verbose_name='Альтернативный текст')),
                ('image', models.ImageField(blank=True, max_length=500, upload_to=core.models.ProjectImages.get_upload_path, verbose_name='Изображение проекта')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.project')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
