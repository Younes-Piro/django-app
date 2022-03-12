from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.TextField()

    def __str__(self):
        return self.title

class Accessory(models.Model):
    titles = models.CharField(max_length=200)
    prices = models.CharField(max_length=10)
    all_reviews = models.CharField(max_length=30)
    total_reviews = models.CharField(max_length=30)

    def __str__(self):
        return self.title