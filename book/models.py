from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="")
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.title