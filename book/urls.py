from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    path("books/", views.book_all, name="book_all"),

    path('books/fantastic', views.books_genre_fantastic, name="books_fantastic"),
    path('books/literature', views.books_genre_literature, name="books_literature"),
    path('books/autobiography', views.books_genre_autobiography, name="books_autobiography"),
    path('books/manga', views.books_genre_manga, name="books_manga"),
    path('books/detective', views.books_genre_detective, name="books_detective"),

    path("books/<int:id>/", views.book_detail, name="book_detail"),
    path("add-book/", views.add_book, name="add_book"),
    path("books/<int:id>/update/", views.update_book, name="update_book"),
    path("books/<int:id>/delete/", views.delete_book, name="delete_book"),
]
