from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.shortcuts import redirect, reverse


def book_all(request):
    books = models.Book.objects.all()
    return render(request, "book_list.html", {"books": books})


def book_detail(request, id):
    book = get_object_or_404(models.Book, id=id)
    return render(request, "book_detail.html", {"book": book})

#======================================================================================

def books_genre_fantastic(request):
    books = models.Book.objects.filter(genre="fantastic").order_by("-id")
    return render(request, "book_list.html", {"books": books})


def books_genre_literature(request):
    books = models.Book.objects.filter(genre="literature").order_by("-id")
    return render(request, "book_list.html", {"books": books})


def books_genre_autobiography(request):
    books = models.Book.objects.filter(genre="autobiography").order_by("-id")
    return render(request, "book_list.html", {"books": books})


def books_genre_manga(request):
    books = models.Book.objects.filter(genre="manga").order_by("-id")
    return render(request, "book_list.html", {"books": books})


def books_genre_detective(request):
    books = models.Book.objects.filter(genre="detective").order_by("-id")
    return render(request, "book_list.html", {"books": books})


#========================================================================================

def add_book(request):
    method = request.method
    if method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("books:book_all"))
    else:
        form = forms.BookForm()
    return render(request, "add_books.html", {'form': form})


def update_book(request, id):
    book_id = get_object_or_404(models.Book, id=id)
    if request.method == "POST":
        form = forms.BookForm(instance=book_id, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("books:book_all"))
    else:
        form = forms.BookForm(instance=book_id)
    return render(request, "books_update.html", {"form": form, "book": book_id})


def delete_book(request, id):
    book_id = get_object_or_404(models.Book, id=id)
    book_id.delete()
    return redirect(reverse("books:book_all"))
