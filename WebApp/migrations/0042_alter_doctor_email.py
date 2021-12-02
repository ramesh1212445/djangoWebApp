# Generated by Django 3.2.9 on 2021-12-02 18:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0041_auto_20211202_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.EmailField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^[\\w#\\-_\\+\\.\\(\\)@~\\\\/*!&]+$', message='Contains some prohibited symbols')]),
        ),
    ]