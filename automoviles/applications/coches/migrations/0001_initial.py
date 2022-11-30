# Generated by Django 4.0.6 on 2022-09-11 18:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('nombre', models.CharField(max_length=35, unique=True, verbose_name='Marca')),
                ('logo', models.ImageField(blank=True, upload_to='imgs', verbose_name='Logo')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('nombre', models.CharField(max_length=35, verbose_name='Nombre')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coches.marca')),
            ],
            options={
                'verbose_name': 'Modelo',
                'verbose_name_plural': 'Modelos',
                'unique_together': {('marca', 'nombre')},
            },
        ),
        migrations.CreateModel(
            name='Coche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('fecha_creacion', models.DateField()),
                ('imagen', models.ImageField(blank=True, upload_to='imgs', verbose_name='Imagen')),
                ('portada', models.BooleanField(default=False)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marca', to='coches.marca')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modelo', to='coches.modelo')),
            ],
            options={
                'verbose_name': 'Coche',
                'verbose_name_plural': 'Coches',
                'unique_together': {('fecha_creacion', 'marca', 'modelo')},
            },
        ),
    ]
