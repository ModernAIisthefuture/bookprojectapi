
from django.db import models


class APIClient(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    api_key = models.CharField(
        max_length=64,
        unique=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class Book(models.Model):

    title = models.CharField(max_length=200)

    author = models.CharField(max_length=100)

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    published_date = models.DateField()

    def __str__(self):
        return self.title
