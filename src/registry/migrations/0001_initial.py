# Generated by Django 4.2.1 on 2023-05-30 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=100)),
                (
                    'email',
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                (
                    'institution',
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=255)),
                (
                    'description',
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ('repository', models.URLField()),
                ('implementation_language', models.CharField(max_length=100)),
                (
                    'type',
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                (
                    'author',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='registry.author',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Model',
                'verbose_name_plural': 'Models',
            },
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'description',
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ('commit', models.CharField(max_length=255)),
                ('predict_date', models.DateField()),
                ('prediction', models.JSONField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                (
                    'model',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='registry.model',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Prediction',
                'verbose_name_plural': 'Predictions',
            },
        ),
    ]
