# Generated by Django 4.2 on 2023-07-10 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctors', '0007_availabilityday_availabilitytime_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='office_appointments', to='doctors.doctoroffice')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient_appointments', to=settings.AUTH_USER_MODEL)),
                ('time', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='availability_appointments', to='doctors.availabilitytime')),
            ],
        ),
    ]
