# Generated by Django 3.0.1 on 2020-04-27 10:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polaroid', '0005_auto_20200427_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(default=datetime.datetime(2020, 4, 27, 15, 35, 51, 981992)),
        ),
    ]