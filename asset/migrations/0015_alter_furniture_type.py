# Generated by Django 4.0.4 on 2022-06-04 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0014_alter_furniture_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='type',
            field=models.CharField(max_length=20),
        ),
    ]