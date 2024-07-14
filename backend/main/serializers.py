from rest_framework import serializers
from . import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = '__all__'


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Audio
        fields = '__all__'


class NarratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Narrator
        fields = '__all__'


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Series
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'
