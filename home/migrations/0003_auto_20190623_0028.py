# Generated by Django 2.1.5 on 2019-06-23 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190201_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fodder',
            name='red_social',
        ),
        migrations.DeleteModel(
            name='Fodder',
        ),
        migrations.DeleteModel(
            name='RedSocial',
        ),
    ]