# Generated by Django 3.0.1 on 2020-05-19 06:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polaroid', '0056_auto_20200518_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posttime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 12, 14, 35, 179113)),
        ),
    ]
