# Generated by Django 3.0.1 on 2020-04-30 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polaroid', '0016_auto_20200430_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profilepic',
            field=models.ImageField(default='default.png', upload_to='profilepics/'),
        ),
    ]