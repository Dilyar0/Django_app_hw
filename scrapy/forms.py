from . import parser, models
from django import forms


class ParserForm(forms.Form):
    MEDIA_CHOICE = (
        ("Anime", "Anime"),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICE)

    class Meta:
        field = [
            "media_type",
        ]

    def parse_data(self):
        if self.data["media_type"] == "Anime":
            anime_parser = parser.parser_func()
            for data in anime_parser:
                models.Anime.objects.create(**data)
