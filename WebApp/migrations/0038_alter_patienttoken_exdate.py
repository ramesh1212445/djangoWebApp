# Generated by Django 3.2.9 on 2021-11-30 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0037_alter_patienttoken_exdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patienttoken',
            name='exdate',
            field=models.DateTimeField(default='$2021-11-30 21:57:46.276728'),
        ),
    ]
