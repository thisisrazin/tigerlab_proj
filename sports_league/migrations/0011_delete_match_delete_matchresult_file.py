# Generated by Django 4.2.4 on 2023-08-12 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports_league', '0010_match'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Match',
        ),
        migrations.DeleteModel(
            name='MatchResult_File',
        ),
    ]
