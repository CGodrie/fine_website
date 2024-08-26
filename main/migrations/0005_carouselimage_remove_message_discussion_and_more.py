# Generated by Django 5.1 on 2024-08-26 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_message_message_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to='carousel_images/')),
                ('order', models.PositiveIntegerField(default=0, help_text="Ordre d'affichage des images")),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.RemoveField(
            model_name='message',
            name='discussion',
        ),
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.DeleteModel(
            name='Discussion',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]