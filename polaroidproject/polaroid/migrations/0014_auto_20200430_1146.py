# Generated by Django 3.0.1 on 2020-04-30 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polaroid', '0013_auto_20200430_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profilepic',
            field=models.ImageField(height_field=106, null=True, upload_to='profilepics/', width_field=106),
        ),
    ]
