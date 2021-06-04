# Generated by Django 3.2.4 on 2021-06-04 23:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('prescriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prescriptions',
            options={'ordering': ['-created_at'], 'verbose_name': 'Prescription', 'verbose_name_plural': 'Prescriptions'},
        ),
        migrations.AddField(
            model_name='prescriptions',
            name='clinic',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prescriptions',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prescriptions',
            name='patient',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prescriptions',
            name='physician',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prescriptions',
            name='text',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='prescriptions',
            table='Prescriptions',
        ),
    ]
