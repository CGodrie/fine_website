# Generated by Django 5.1 on 2024-11-01 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_agfile_meeting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
