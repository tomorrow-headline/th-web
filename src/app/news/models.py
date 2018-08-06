from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    excerpt = models.TextField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
