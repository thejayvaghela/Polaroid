# Generated by Django 3.0.1 on 2020-04-28 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polaroid', '0010_auto_20200428_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profilepic',
            field=models.ImageField(null=True, upload_to='profilepics/'),
        ),
    ]