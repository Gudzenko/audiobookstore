from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
import os


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='authors_photos/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Audio(models.Model):
    title = models.CharField(max_length=200)
    file_path = models.FileField(upload_to='audio_files/')

    def __str__(self):
        return self.title


class Narrator(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, blank=True)
    series = models.CharField(max_length=200, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    narrator = models.ForeignKey(Narrator, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=True)
    audio_files = models.ManyToManyField(Audio, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    illustration = models.ImageField(upload_to='book_illustrations/', blank=True, null=True)

    def __str__(self):
        return self.title


@receiver(pre_delete, sender=Author)
@receiver(pre_delete, sender=Audio)
@receiver(pre_delete, sender=Book)
def delete_files(sender, instance, **kwargs):
    if isinstance(instance, Audio):
        if instance.file_path:
            if os.path.isfile(instance.file_path.path):
                os.remove(instance.file_path.path)
    elif isinstance(instance, Book):
        if instance.illustration:
            if os.path.isfile(instance.illustration.path):
                os.remove(instance.illustration.path)
    elif isinstance(instance, Author):
        if instance.photo:
            if os.path.isfile(instance.photo.path):
                os.remove(instance.photo.path)


@receiver(pre_save, sender=Author)
@receiver(pre_save, sender=Audio)
@receiver(pre_save, sender=Book)
def delete_old_files_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return

    if isinstance(instance, Audio):
        if old_instance.file_path and old_instance.file_path != instance.file_path:
            if os.path.isfile(old_instance.file_path.path):
                os.remove(old_instance.file_path.path)
    elif isinstance(instance, Book):
        if old_instance.illustration and old_instance.illustration != instance.illustration:
            if os.path.isfile(old_instance.illustration.path):
                os.remove(old_instance.illustration.path)
    elif isinstance(instance, Author):
        if old_instance.photo and old_instance.photo != instance.photo:
            if os.path.isfile(old_instance.photo.path):
                os.remove(old_instance.photo.path)
