from django.db import models


class Anime(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(max_length=250)

    def __str__(self):
        return self.title
