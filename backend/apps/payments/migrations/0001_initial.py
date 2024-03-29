# Generated by Django 4.2 on 2023-07-18 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MonetaryTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=[('IRR', 'ریال ایران'), ('IRT', 'تومان ایران')], default='IRR', max_length=3)),
                ('track_number', models.CharField()),
                ('status', models.CharField(choices=[('Complete', 'complete'), ('Error', 'error'), ('Pending', 'pending'), ('Canceled', 'canceled')], default='pending')),
                ('reference_number', models.CharField(blank=True, null=True)),
                ('response_result', models.TextField(blank=True, null=True)),
                ('extra_information', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('by_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='by_transactions', to=settings.AUTH_USER_MODEL)),
                ('for_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='for_transactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
