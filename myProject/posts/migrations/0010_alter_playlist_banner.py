# Generated by Django 5.0.7 on 2024-08-10 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_playlist_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='banner',
            field=models.ImageField(blank=True, default='fallback.jpg', upload_to='playlistImages'),
        ),
    ]
