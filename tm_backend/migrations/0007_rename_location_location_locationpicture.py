# Generated by Django 3.2.6 on 2023-01-09 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tm_backend', '0006_auto_20230109_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='location',
            new_name='locationPicture',
        ),
    ]