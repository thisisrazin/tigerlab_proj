# Generated by Django 4.2.4 on 2023-08-13 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sports_league', '0017_delete_ranking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=200)),
                ('points', models.IntegerField()),
                ('resultFile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sports_league.matchresult_file')),
            ],
        ),
    ]