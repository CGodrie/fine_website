# Generated by Django 5.1 on 2024-08-30 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_learningresources'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learningresources',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
