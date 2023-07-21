# Generated by Django 4.2 on 2023-07-17 20:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_alter_appointment_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='uuid',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, unique=True),
        ),
    ]