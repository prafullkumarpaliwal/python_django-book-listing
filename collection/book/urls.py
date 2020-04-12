from django.urls import path

from .views import (BookListCreate, BookRetrieveUpdateDestroy, BookUserListCreate, BookUserRetrieveUpdateDestroy)


urlpatterns = [
    path('book/', BookListCreate.as_view()),
    path('book/<int:pk>/', BookRetrieveUpdateDestroy.as_view()),

    path('book-user/', BookUserListCreate.as_view()),
    path('book-user/<int:pk>/', BookUserRetrieveUpdateDestroy.as_view()),
    ]