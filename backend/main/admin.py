from django.contrib import admin
from . import models


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'description')


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_path')


@admin.register(models.Narrator)
class NarratorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(models.Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'series', 'number', 'narrator', 'available', 'created_at')
    filter_horizontal = ('authors', 'audio_files', 'genres')
