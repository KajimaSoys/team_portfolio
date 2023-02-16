# Generated by Django 4.1.7 on 2023-02-16 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_project_description_short_ru_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='group',
        ),
        migrations.AddField(
            model_name='project',
            name='group',
            field=models.ManyToManyField(to='core.group', verbose_name='Группа'),
        ),
    ]