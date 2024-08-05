from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import viewsets
from . import views

router = DefaultRouter()
router.register(r'authors', viewsets.AuthorViewSet)
router.register(r'genres', viewsets.GenreViewSet)
router.register(r'audios', viewsets.AudioViewSet)
router.register(r'narrators', viewsets.NarratorViewSet)
router.register(r'books', viewsets.BookViewSet)
router.register(r'series', viewsets.SeriesViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('genres/', views.genre_list, name='genre_list'),
    path('narrators/', views.narrator_list, name='narrator_list'),
    path('series/', views.series_list, name='series_list'),
    path('', include(router.urls)),
]