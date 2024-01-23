# models.py
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255,default='my_video')
    description = models.TextField(default='abc')
    privacy_status = models.CharField(max_length=20,default='private')
    owner_channel_id = models.CharField(max_length=50,default='123')
    video_path = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.title
