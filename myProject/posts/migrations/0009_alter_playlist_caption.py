# Generated by Django 5.0.7 on 2024-08-10 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_playlist_playlistid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='caption',
            field=models.TextField(),
        ),
    ]
