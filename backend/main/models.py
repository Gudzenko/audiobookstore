from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver


def audio_file_path(instance, filename):
    try:
        author_name = f"{instance.book.authors.first().last_name}_{instance.book.authors.first().first_name}" \
            if instance.book.authors.exists() else 'unknown_author'
        book_title = instance.book.title if instance.book else 'unknown_book'
        return f'audio_files/{author_name}/{book_title}/{filename}'
    except Exception:
        return f'audio_files/{filename}'


def author_photo_file_path(instance, filename):
    try:
        author_name = f"{instance.last_name}_{instance.first_name}"
        return f'author_photo/{author_name}/{filename}'
    except Exception:
        return f'author_photo/undefined_author/{filename}'


def book_illustrations_file_path(instance, filename):
    try:
        book_title = instance.title
        return f'book_illustrations_files/{book_title}/{filename}'
    except Exception:
        return f'book_illustrations_files/undefined_book/{filename}'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=author_photo_file_path, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Audio(models.Model):
    title = models.CharField(max_length=200)
    file_path = models.FileField(upload_to=audio_file_path)

    def __str__(self):
        return self.title


class Narrator(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Series(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, blank=True)
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True, blank=True)
    number = models.IntegerField(blank=True, null=True)
    narrator = models.ForeignKey(Narrator, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=False)
    audio_files = models.ManyToManyField(Audio, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    illustration = models.ImageField(upload_to=book_illustrations_file_path, blank=True, null=True)

    def __str__(self):
        return self.title


@receiver(pre_delete, sender=Author)
@receiver(pre_delete, sender=Audio)
@receiver(pre_delete, sender=Book)
def delete_files(sender, instance, **kwargs):
    if isinstance(instance, Audio):
        if instance.file_path:
            storage, path = instance.file_path.storage, instance.file_path.name
            storage.delete(path)
    elif isinstance(instance, Book):
        if instance.illustration:
            storage, path = instance.illustration.storage, instance.illustration.name
            storage.delete(path)
    elif isinstance(instance, Author):
        if instance.photo:
            storage, path = instance.photo.storage, instance.photo.name
            storage.delete(path)


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
            storage, path = old_instance.file_path.storage, old_instance.file_path.name
            storage.delete(path)
    elif isinstance(instance, Book):
        if old_instance.illustration and old_instance.illustration != instance.illustration:
            storage, path = old_instance.illustration.storage, old_instance.illustration.name
            storage.delete(path)
    elif isinstance(instance, Author):
        if old_instance.photo and old_instance.photo != instance.photo:
            storage, path = old_instance.photo.storage, old_instance.photo.name
            storage.delete(path)
