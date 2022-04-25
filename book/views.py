from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.shortcuts import redirect, reverse


def book_all(request):
    books = models.Book.objects.all()
    return render(request, "book_list.html", {"books": books})


def book_detail(request, id):
    book = get_object_or_404(models.Book, id=id)
    return render(request, "book_detail.html", {"book": book})


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
