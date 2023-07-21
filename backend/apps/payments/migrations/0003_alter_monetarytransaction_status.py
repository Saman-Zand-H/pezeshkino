# Generated by Django 4.2 on 2023-07-18 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_monetarytransaction_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monetarytransaction',
            name='status',
            field=models.CharField(choices=[('Complete', 'complete'), ('Error', 'error'), ('Pending', 'pending'), ('Canceled', 'canceled'), ('Not Started', 'not_started')], default='not_started'),
        ),
    ]