# Generated by Django 4.2.3 on 2023-08-09 14:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comunas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionalidades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Regiones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('ordinal', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=10)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('correo', models.CharField(blank=True, max_length=50, null=True)),
                ('estado', models.IntegerField(default=0)),
                ('cargo', models.ForeignKey(db_column='cargo', on_delete=django.db.models.deletion.CASCADE, related_name='usuario_cargo', to='core.cargos')),
            ],
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provincia_region', to='core.regiones')),
            ],
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('correo', models.CharField(max_length=50)),
                ('sexo', models.IntegerField(choices=[(1, 'Masculino'), (2, 'Femenino')], default=1)),
                ('fecha_nacimiento', models.DateField(default=datetime.date(2000, 1, 1))),
                ('anteojos', models.CharField(max_length=10)),
                ('estado', models.IntegerField(choices=[(0, 'Sin estado'), (1, 'Activo'), (2, 'Suspendido'), (3, 'Suspendido')], default=0)),
                ('dominio_ingles', models.IntegerField(choices=[(0, 'Sin estado'), (1, 'Básico'), (2, 'Medio'), (3, 'Avanzado'), (4, 'Nativo')], default=0)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persona_comuna', to='core.comunas')),
            ],
        ),
        migrations.CreateModel(
            name='Permisos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permiso', models.IntegerField(default=0)),
                ('funcionalidad', models.ForeignKey(db_column='funcionalidad', on_delete=django.db.models.deletion.CASCADE, related_name='permiso_funcionalidad', to='core.funcionalidades')),
                ('usuario', models.ForeignKey(db_column='usuario', on_delete=django.db.models.deletion.CASCADE, related_name='permiso_usuario', to='core.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Perfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permiso', models.IntegerField(default=0)),
                ('cargo', models.ForeignKey(db_column='cargo', on_delete=django.db.models.deletion.CASCADE, related_name='perfil_cargo', to='core.cargos')),
                ('funcionalidad', models.ForeignKey(db_column='funcionalidad', on_delete=django.db.models.deletion.CASCADE, related_name='perfil_funcionalidad', to='core.funcionalidades')),
            ],
        ),
        migrations.AddIndex(
            model_name='funcionalidades',
            index=models.Index(fields=['descripcion'], name='funcionalidades_descripcion'),
        ),
        migrations.AddField(
            model_name='comunas',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comuna_provincia', to='core.provincias'),
        ),
        migrations.AddIndex(
            model_name='cargos',
            index=models.Index(fields=['nombre'], name='cargos_descripcion'),
        ),
        migrations.AddIndex(
            model_name='usuarios',
            index=models.Index(fields=['nombre'], name='usuario_nombre'),
        ),
        migrations.AddIndex(
            model_name='permisos',
            index=models.Index(fields=['usuario'], name='permiso_usuario'),
        ),
        migrations.AddIndex(
            model_name='permisos',
            index=models.Index(fields=['funcionalidad'], name='permiso_funcionalidad'),
        ),
        migrations.AlterUniqueTogether(
            name='permisos',
            unique_together={('usuario', 'funcionalidad', 'permiso')},
        ),
        migrations.AddIndex(
            model_name='perfiles',
            index=models.Index(fields=['funcionalidad'], name='perfil_funcionalidad2'),
        ),
        migrations.AlterUniqueTogether(
            name='perfiles',
            unique_together={('cargo', 'funcionalidad', 'permiso')},
        ),
    ]