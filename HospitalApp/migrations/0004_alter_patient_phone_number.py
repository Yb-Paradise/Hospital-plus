# Generated by Django 5.1.6 on 2025-02-27 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0003_alter_patient_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.IntegerField(max_length=11),
        ),
    ]
