from django.urls import path
from . import views


app_name = "books"
urlpatterns = [
    path("books/", views.book_all, name="book_all"),
    path("books/<int:id>/", views.book_detail, name="book_detail"),
    path("add-book/", views.add_book, name="add-book")
]
