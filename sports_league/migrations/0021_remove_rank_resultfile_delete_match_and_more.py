# Generated by Django 4.2.4 on 2023-08-13 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports_league', '0020_alter_matchresult_file_documentcsv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rank',
            name='resultFile',
        ),
        migrations.DeleteModel(
            name='Match',
        ),
        migrations.DeleteModel(
            name='MatchResult_File',
        ),
        migrations.DeleteModel(
            name='Rank',
        ),
    ]
