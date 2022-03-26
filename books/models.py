from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.TextField()

    def __str__(self):
        return self.title

class Accessory(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    all_review = models.CharField(max_length=30)
    total_review = models.CharField(max_length=30)

    def __str__(self):
        return self.title