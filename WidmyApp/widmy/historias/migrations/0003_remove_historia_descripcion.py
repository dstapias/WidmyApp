# Generated by Django 3.2.6 on 2023-05-08 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0002_alter_historia_documento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historia',
            name='descripcion',
        ),
    ]