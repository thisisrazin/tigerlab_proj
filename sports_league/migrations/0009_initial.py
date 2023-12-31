# Generated by Django 4.2.4 on 2023-08-12 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sports_league', '0008_delete_matchresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchResult_File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documentCSV', models.FileField(upload_to='sports_league/documentCSV/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
