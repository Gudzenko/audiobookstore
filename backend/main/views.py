from django.shortcuts import render
from . import models


def index(request):
    return render(request, 'main/index.html')


def author_list(request):
    authors = models.Author.objects.all().order_by('last_name')
    return render(request, 'main/tile_list.html', {
        'title': 'Авторы',
        'items': [{'title': f'{author.first_name} {author.last_name}', 'image': author.photo} for author in authors]
    })


def book_list(request):
    books = models.Book.objects.all().order_by('title')
    return render(request, 'main/tile_list.html', {
        'title': 'Книги',
        'items': [{'title': book.title, 'image': book.illustration} for book in books]
    })


def genre_list(request):
    genres = models.Genre.objects.all().order_by('name')
    return render(request, 'main/genre_list.html', {'genres': genres})


def narrator_list(request):
    narrators = models.Narrator.objects.all().order_by('last_name')
    return render(request, 'main/narrator_list.html', {'narrators': narrators})


def series_list(request):
    series = models.Series.objects.all().order_by('name')
    return render(request, 'main/series_list.html', {'series': series})
