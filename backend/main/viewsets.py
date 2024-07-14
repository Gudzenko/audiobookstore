from rest_framework import viewsets
from . import models
from . import serializers


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class AudioViewSet(viewsets.ModelViewSet):
    queryset = models.Audio.objects.all()
    serializer_class = serializers.AudioSerializer


class NarratorViewSet(viewsets.ModelViewSet):
    queryset = models.Narrator.objects.all()
    serializer_class = serializers.NarratorSerializer


class SeriesViewSet(viewsets.ModelViewSet):
    queryset = models.Series.objects.all()
    serializer_class = serializers.SeriesSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
