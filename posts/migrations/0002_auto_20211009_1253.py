# Generated by Django 3.2.8 on 2021-10-09 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post1',
            name='slug',
        ),
        migrations.AlterField(
            model_name='post1',
            name='author',
            field=models.ForeignKey(default=posts.models.generate_id, on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL),
        ),
    ]
