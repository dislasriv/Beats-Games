# Generated by Django 5.0.7 on 2024-08-15 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_playlist_songs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='banner',
        ),
        migrations.AddField(
            model_name='playlist',
            name='bannerUrl',
            field=models.TextField(default='if youre seeing this there is an error, start at posts/models.py'),
        ),
    ]