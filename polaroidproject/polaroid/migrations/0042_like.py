# Generated by Django 3.0.1 on 2020-05-15 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polaroid', '0041_delete_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('likeid', models.AutoField(primary_key=True, serialize=False)),
                ('liked_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='liked_by', to='polaroid.User')),
                ('post_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to='polaroid.User')),
                ('postid', models.ManyToManyField(to='polaroid.Post')),
            ],
        ),
    ]
