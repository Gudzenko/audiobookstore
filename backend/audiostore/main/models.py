from datetime import datetime, time, timedelta
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
# Create your models here.


class Audio(models.Model):
    audio_name = models.CharField('audio_name', max_length=250)
    audio_file = models.FileField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.audio_name}/{self.audio_file}/{self.created_at}"


@receiver(pre_delete, sender=Audio)
def delete_audio_file(sender, instance, **kwargs):
    instance.audio_file.delete(False)

