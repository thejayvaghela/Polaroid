# Generated by Django 3.0.1 on 2020-04-27 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polaroid', '0004_auto_20200427_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]