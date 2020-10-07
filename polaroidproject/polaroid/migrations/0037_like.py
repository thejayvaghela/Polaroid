# Generated by Django 3.0.1 on 2020-05-14 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polaroid', '0036_auto_20200510_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('likeid', models.AutoField(primary_key=True, serialize=False)),
                ('postid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polaroid.Post')),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polaroid.User')),
            ],
        ),
    ]
