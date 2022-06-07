# Generated by Django 4.0.4 on 2022-06-07 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0022_remove_electronic_id_alter_electronic_serial_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
                ('initial_value', models.IntegerField()),
                ('apreciation_rate', models.DecimalField(decimal_places=2, max_digits=100, null=True)),
                ('current_value', models.IntegerField(null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.location')),
            ],
        ),
    ]
