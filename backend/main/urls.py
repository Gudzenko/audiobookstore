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
    path('', include(router.urls)),
]