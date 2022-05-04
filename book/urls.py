from django.urls import path
from . import views, models


app_name = "books"
urlpatterns = [
    path("books/", views.BookListView.as_view(), name="book_all"),

    path('books/fantastic', views.BookListView.as_view(
        queryset=models.Book.objects.filter(genre="fantastic")
    ), name="books_fantastic"),
    path('books/literature', views.BookListView.as_view(
        queryset=models.Book.objects.filter(genre="literature")
    ), name="books_literature"),
    path('books/autobiography', views.BookListView.as_view(
        queryset=models.Book.objects.filter(genre="autobiography")
    ), name="books_autobiography"),
    path('books/manga', views.BookListView.as_view(
        queryset=models.Book.objects.filter(genre="manga")
    ), name="books_manga"),
    path('books/detective', views.BookListView.as_view(
        queryset=models.Book.objects.filter(genre="detective")
    ), name="books_detective"),

    path("books/<int:id>/", views.BookDetailView.as_view(), name="book_detail"),
    path("add-book/", views.BooksAddView.as_view(), name="add_book"),
    path("books/<int:id>/update/", views.BooksUpdateView.as_view(), name="update_book"),
    path("books/<int:id>/delete/", views.BooksDeleteView.as_view(), name="delete_book"),
]
