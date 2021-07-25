# Generated by Django 3.1.7 on 2021-05-02 16:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20210502_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic', models.CharField(choices=[('DCH', 'Dhaka Community Hospital'), ('JEWMCH', 'Japan East West Medical College Hospital, Dhaka'), ('EHD', 'Evercare Hospital, Dhaka')], max_length=100)),
                ('date', models.DateField(default=datetime.datetime(2021, 5, 2, 16, 27, 35, 939075, tzinfo=utc))),
                ('time', models.DateField(default=datetime.datetime(2021, 5, 2, 16, 27, 35, 939075, tzinfo=utc))),
            ],
        ),
    ]
