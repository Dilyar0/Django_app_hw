from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from . import models, forms


class ParserFormView(generic.FormView):
    template_name = "parser.html"
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parse_data()
            # return HttpResponse("Parse data success")
            return redirect(reverse("anime:anime_list"))
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)


class AnimeListView(generic.ListView):
    template_name = "anime.html"
    queryset = models.Anime.objects.all()

    def get_queryset(self):
        return self.queryset
