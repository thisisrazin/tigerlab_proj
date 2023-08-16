# Generated by Django 4.2.4 on 2023-08-12 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sports_league', '0009_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamOne', models.CharField(max_length=200)),
                ('teamTwo', models.CharField(max_length=200)),
                ('teamOneScore', models.IntegerField()),
                ('teamTwoScore', models.IntegerField()),
                ('resultFile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sports_league.matchresult_file')),
            ],
        ),
    ]
