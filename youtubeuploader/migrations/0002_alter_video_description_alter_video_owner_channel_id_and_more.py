# Generated by Django 5.0.1 on 2024-01-22 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeuploader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(default='abc'),
        ),
        migrations.AlterField(
            model_name='video',
            name='owner_channel_id',
            field=models.CharField(default='123', max_length=50),
        ),
        migrations.AlterField(
            model_name='video',
            name='privacy_status',
            field=models.CharField(default='private', max_length=20),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(default='my_video', max_length=255),
        ),
    ]
