# Generated by Django 4.0.4 on 2022-06-05 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0016_alter_furniture_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='current_value',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='depreciation_rate',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='initial_value',
            field=models.IntegerField(),
        ),
    ]
