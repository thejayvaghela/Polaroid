# Generated by Django 3.0.1 on 2020-04-27 10:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polaroid', '0006_auto_20200427_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(default=datetime.date(1997, 10, 19)),
        ),
    ]
