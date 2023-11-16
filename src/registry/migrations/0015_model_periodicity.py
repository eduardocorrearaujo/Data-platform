# Generated by Django 4.2.5 on 2023-11-07 18:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("registry", "0014_remove_prediction_adm_level_model_adm_level"),
    ]

    operations = [
        migrations.AddField(
            model_name="model",
            name="periodicity",
            field=models.CharField(
                choices=[
                    ("daily", "Daily"),
                    ("weekly", "Weekly"),
                    ("monthly", "Monthly"),
                    ("yearly", "Yearly"),
                ],
                null=True,
            ),
        ),
    ]