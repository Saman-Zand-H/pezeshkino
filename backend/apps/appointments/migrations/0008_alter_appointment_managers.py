# Generated by Django 4.2 on 2023-07-23 19:51

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0007_alter_appointment_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='appointment',
            managers=[
                ('paid_appointments', django.db.models.manager.Manager()),
            ],
        ),
    ]
