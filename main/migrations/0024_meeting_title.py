# Generated by Django 5.1 on 2024-11-01 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_meeting_end_time_alter_meeting_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='title',
            field=models.CharField(default='Réunion', max_length=255),
        ),
    ]
