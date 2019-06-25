# Generated by Django 2.1.5 on 2019-06-25 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0006_auto_20190624_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Caracteristica',
                'verbose_name_plural': 'Caracteristicas',
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/proyecto')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(help_text='descripción corta del proyecto')),
                ('url', models.URLField(blank=True, help_text='Página web del proyecto.', null=True)),
                ('caracteristica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenido.Caracteristica')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
            },
        ),
        migrations.AlterModelOptions(
            name='aboutme',
            options={'verbose_name': 'About', 'verbose_name_plural': 'Abouts'},
        ),
        migrations.AlterModelOptions(
            name='galeria',
            options={'verbose_name': 'Galeria', 'verbose_name_plural': 'Galerias'},
        ),
    ]