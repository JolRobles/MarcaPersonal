# Generated by Django 2.1.5 on 2019-06-25 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0007_auto_20190624_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='nuevo',
            field=models.BooleanField(default=True),
        ),
    ]
