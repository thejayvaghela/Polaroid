# Generated by Django 3.0.1 on 2020-05-15 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polaroid', '0043_auto_20200515_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='postid',
        ),
        migrations.AddField(
            model_name='like',
            name='postid',
            field=models.ManyToManyField(to='polaroid.Post'),
        ),
    ]
