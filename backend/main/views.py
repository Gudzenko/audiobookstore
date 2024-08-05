from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from . import models


def index(request):
    return render(request, 'main/index.html')


def author_list(request):
    authors = models.Author.objects.all().order_by('last_name')
    return render(request, 'main/tile_list.html', {
        'title': 'Авторы',
        'items': [{
            'title': f'{author.first_name} {author.last_name}',
            'image': author.photo,
            'url': reverse('author_detail', args=[author.id])
        } for author in authors]
    })


def author_detail(request, author_id):
    author = get_object_or_404(models.Author, pk=author_id)
    books = models.Book.objects.filter(authors=author).order_by('title')
    return render(request, 'main/author_detail.html', {'author': author, 'books': books})


def book_list(request):
    books = models.Book.objects.all().order_by('title')
    return render(request, 'main/tile_list.html', {
        'title': 'Книги',
        'items': [{
            'title': book.title,
            'image': book.illustration,
            'url': reverse('book_detail', args=[book.id]),
        } for book in books]
    })


def book_detail(request, book_id):
    book = get_object_or_404(models.Book, pk=book_id)
    return render(request, 'main/book_detail.html', {'book': book})


def genre_list(request):
    genres = models.Genre.objects.all().order_by('name')
    return render(request, 'main/genre_list.html', {'genres': genres})


def narrator_list(request):
    narrators = models.Narrator.objects.all().order_by('last_name')
    return render(request, 'main/narrator_list.html', {'narrators': narrators})


def series_list(request):
    series = models.Series.objects.all().order_by('name')
    return render(request, 'main/series_list.html', {'series': series})
