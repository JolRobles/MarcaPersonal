# Generated by Django 2.1.5 on 2019-06-25 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0009_auto_20190624_2319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caracteristica',
            old_name='nombre',
            new_name='caracteristica',
        ),
    ]