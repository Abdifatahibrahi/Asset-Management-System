# Generated by Django 4.0.4 on 2022-06-04 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0011_alter_furniture_date_alter_furniture_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='furniture',
            name='id',
        ),
        migrations.AlterField(
            model_name='furniture',
            name='serial_no',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
