# Generated by Django 4.0.1 on 2022-03-14 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_song_listened'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='listened',
            field=models.BigIntegerField(default=0),
        ),
    ]
