# Generated by Django 4.0.4 on 2022-06-04 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0012_remove_furniture_id_alter_furniture_serial_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='serial_no',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]