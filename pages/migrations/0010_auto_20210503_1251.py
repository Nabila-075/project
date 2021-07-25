# Generated by Django 3.1.7 on 2021-05-03 06:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20210502_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccine',
            name='costing',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 5, 3, 6, 51, 41, 359472, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 3, 6, 51, 41, 359472, tzinfo=utc)),
        ),
        migrations.AlterModelTable(
            name='appointment',
            table=None,
        ),
    ]
