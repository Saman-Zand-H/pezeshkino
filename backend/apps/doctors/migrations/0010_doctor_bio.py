# Generated by Django 4.2 on 2023-07-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0009_onlineappointmentspecifics_onlineavailabilityday_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
