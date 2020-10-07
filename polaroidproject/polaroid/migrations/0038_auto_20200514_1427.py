# Generated by Django 3.0.1 on 2020-05-14 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polaroid', '0037_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='user_email',
        ),
        migrations.AddField(
            model_name='like',
            name='liked_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='liked_by', to='polaroid.User'),
        ),
        migrations.AddField(
            model_name='like',
            name='post_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to='polaroid.User'),
        ),
    ]
