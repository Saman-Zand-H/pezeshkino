# Generated by Django 4.2 on 2023-05-13 23:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="usermodel",
            name="user_type",
            field=models.CharField(
                choices=[("D", "Doctor"), ("S", "Secretary"), ("P", "Patience")],
                default="P",
                max_length=1,
            ),
        ),
    ]
