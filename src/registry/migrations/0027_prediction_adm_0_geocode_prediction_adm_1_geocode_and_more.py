# Generated by Django 4.2.11 on 2024-05-08 13:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("registry", "0026_merge_20240507_2315"),
    ]

    operations = [
        migrations.AddField(
            model_name="prediction",
            name="adm_0_geocode",
            field=models.CharField(default="BRA", max_length=3, null=True),
        ),
        migrations.AddField(
            model_name="prediction",
            name="adm_1_geocode",
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="prediction",
            name="adm_3_geocode",
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name="implementationlanguage",
            name="svg_path",
            field=models.FilePathField(
                match=".svg$",
                null=True,
                path="/opt/services/mosqlimate/staticfiles/img/plangs",
            ),
        ),
        migrations.AlterField(
            model_name="prediction",
            name="metadata",
            field=models.CharField(default=None, null=True),
        ),
    ]