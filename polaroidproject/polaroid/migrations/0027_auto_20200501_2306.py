# Generated by Django 3.0.1 on 2020-05-01 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polaroid', '0026_auto_20200501_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profilepic',
            field=models.ImageField(default='default.jpg', upload_to='profilepics/'),
        ),
    ]