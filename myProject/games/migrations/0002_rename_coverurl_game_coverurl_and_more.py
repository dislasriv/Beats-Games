# Generated by Django 5.0.7 on 2024-08-18 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='coverURL',
            new_name='coverUrl',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='releaseDate',
            new_name='releaseYear',
        ),
    ]
