# Generated by Django 3.0.1 on 2020-04-28 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polaroid', '0009_auto_20200427_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profilepic',
            field=models.ImageField(null=True, upload_to='profilepics'),
        ),
    ]