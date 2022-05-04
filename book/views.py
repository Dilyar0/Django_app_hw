from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.shortcuts import redirect, reverse
from django.views import generic


class BookListView(generic.ListView):
    template_name = "book_list.html"
    queryset = models.Book.objects.order_by("-id")

    def get_queryset(self):
        return self.queryset


class BookDetailView(generic.DetailView):
    template_name = "book_detail.html"

    def get_object(self, **kwargs):
        shows_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=shows_id)


# ========================================================================================
class BooksAddView(generic.CreateView):
    template_name = "add_books.html"
    form_class = forms.BookForm
    queryset = models.Book.objects.all()
    success_url = "/books/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BooksAddView, self).form_valid(form=form)


class BooksUpdateView(generic.UpdateView):
    template_name = "books_update.html"
    form_class = forms.BookForm
    success_url = "/books/"

    def get_object(self, **kwargs):
        shows_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=shows_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BooksUpdateView, self).form_valid(form=form)


class BooksDeleteView(generic.DeleteView):
    success_url = "/books/"
    template_name = "confirm_delete_book.html"

    def get_object(self, **kwargs):
        shows_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=shows_id)
