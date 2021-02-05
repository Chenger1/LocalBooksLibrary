from django.db import models

from ebooks.models import Ebook


class Author(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ['name']
        db_table = 'author'


class Book(models.Model):
    WORST_RATE = 1
    BAD_RATE = 2
    MORE_OR_LESS_RATE = 3
    GOOD_RATE = 4
    PERFECT_RATE = 5

    RATE_CHOICES = (
        (WORST_RATE, 'Worst'),
        (BAD_RATE, 'Bad'),
        (MORE_OR_LESS_RATE, 'More or less'),
        (GOOD_RATE, 'Good'),
        (PERFECT_RATE, 'Perfect')
    )

    title = models.CharField(max_length=250)
    author = models.ManyToManyField(Author, related_name='books', blank=True)
    annotation = models.TextField(max_length=500, blank=True)
    genre = models.CharField(max_length=50, blank=True)

    rate = models.IntegerField(choices=RATE_CHOICES, blank=True)

    review = models.TextField(blank=True)

    to_read = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    have_read = models.BooleanField(default=False)

    ebook = models.ForeignKey(Ebook, related_name='ebook', blank=True, null=True,
                              on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']
        db_table = 'book'
