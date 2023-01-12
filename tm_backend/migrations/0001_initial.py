# Generated by Django 3.2.6 on 2022-11-09 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TruckTypeMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('truck_type', models.CharField(blank=True, max_length=150, null=True)),
                ('max_volumne', models.CharField(blank=True, max_length=50, null=True)),
                ('max_weight', models.CharField(blank=True, max_length=50, null=True)),
                ('engine_capacity', models.CharField(blank=True, max_length=50, null=True)),
                ('wheels', models.CharField(blank=True, max_length=50, null=True)),
                ('fuel_capacity', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(blank=True, max_length=150, null=True)),
                ('model', models.CharField(blank=True, max_length=150, null=True)),
                ('truck_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tm_backend.trucktypemaster')),
            ],
        ),
    ]
