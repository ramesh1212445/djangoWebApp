# Generated by Django 3.2.9 on 2021-11-30 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0014_alter_patienttoken_expirydate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patienttoken',
            name='expiryDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 30, 21, 35, 20, 559494)),
        ),
    ]