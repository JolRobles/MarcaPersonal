# Generated by Django 2.1.5 on 2019-06-24 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0002_blog_fecha_creacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, null=True)),
                ('contenido', models.TextField(help_text='comentario dela foto', null=True)),
                ('fecha_creacion', models.DateField(null=True)),
            ],
        ),
    ]
