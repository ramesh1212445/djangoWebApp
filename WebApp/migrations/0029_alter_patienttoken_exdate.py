# Generated by Django 3.2.9 on 2021-11-30 16:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0028_alter_patienttoken_exdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patienttoken',
            name='exdate',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 30, 21, 38, 34, 844485)),
        ),
    ]
