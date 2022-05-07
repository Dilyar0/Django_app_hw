from django.urls import path
from . import views, models

app_name = "anime"
urlpatterns = [
    path("parser/", views.ParserFormView.as_view(), name="parser"),
    path("anime-list/", views.AnimeListView.as_view(
        queryset=models.Anime.objects.order_by("-id")
    ), name="anime_list"),
]
