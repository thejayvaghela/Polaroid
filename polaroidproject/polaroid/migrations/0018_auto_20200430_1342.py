# Generated by Django 3.0.1 on 2020-04-30 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polaroid', '0017_auto_20200430_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profilepic',
            field=models.ImageField(default='/media/default.png', upload_to='profilepics/'),
        ),
    ]
