# Generated by Django 4.0.4 on 2022-06-06 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0020_alter_electronic_initial_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electronic',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='electronic',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]
