# Generated by Django 3.2.6 on 2023-01-03 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tm_backend', '0004_locationpicture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='division_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tm_backend.division'),
        ),
        migrations.AddField(
            model_name='location',
            name='division_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tm_backend.division'),
        ),
        migrations.AddField(
            model_name='thana',
            name='division_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tm_backend.division'),
        ),
        migrations.AddField(
            model_name='union',
            name='division_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tm_backend.division'),
        ),
    ]
