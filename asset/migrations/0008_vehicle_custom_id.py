# Generated by Django 4.0.4 on 2022-05-31 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0007_vehicle_current_value_vehicle_depreciation_rate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='custom_id',
            field=models.IntegerField(null=True),
        ),
    ]
