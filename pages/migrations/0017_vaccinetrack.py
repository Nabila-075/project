# Generated by Django 3.1.7 on 2021-05-22 08:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20210521_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='VaccineTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_administered', models.DateField(default=datetime.date.today)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.useraccount')),
                ('vaccine_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.vaccine')),
            ],
            options={
                'ordering': ['username'],
            },
        ),
    ]