from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="")
    author = models.CharField(max_length=70, default='')
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class BookFeedBack(models.Model):
    text = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    books = models.ForeignKey(Book,
                              on_delete=models.CASCADE,
                              related_name="Book_feed_back")

    def __str__(self):
        return self.books.title
