# Generated by Django 3.1.7 on 2021-05-21 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_scheduleappoint_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleappoint',
            name='clinic',
            field=models.CharField(choices=[('Dhaka Community Hospital', 'Dhaka Community Hospital'), ('Japan East West Medical College Hospital, Dhaka', 'Japan East West Medical College Hospital, Dhaka'), ('Evercare Hospital, Dhaka', 'Evercare Hospital, Dhaka')], max_length=100),
        ),
        migrations.AlterField(
            model_name='scheduleappoint',
            name='time',
            field=models.CharField(choices=[('Morning', 'Morning'), ('Evening', 'Evening')], default='n/a', max_length=100),
        ),
    ]