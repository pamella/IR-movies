# Generated by Django 2.2.7 on 2019-11-21 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movie_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='genre',
            new_name='genres',
        ),
    ]