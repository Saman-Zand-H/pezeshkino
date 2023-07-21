# Generated by Django 4.2 on 2023-07-18 13:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monetarytransaction',
            name='uuid',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, unique=True),
        ),
    ]