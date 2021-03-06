# Generated by Django 3.1.5 on 2021-01-21 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamer_zone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamebooked',
            name='game_time_start',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='item_type',
            field=models.CharField(blank=True, choices=[('chats', 'chats'), ('snacks', 'snacks'), ('drinks', 'drinks'), ('others', 'others')], max_length=100, null=True),
        ),
    ]
