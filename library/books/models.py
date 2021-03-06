from django.db import models
from django.shortcuts import reverse


class Author(models.Model):
    name = models.CharField(max_length=250, blank=True)
    surname = models.CharField(max_length=250)

    class Meta:
        ordering = ['name']
        db_table = 'author'

    def get_absolute_url(self):
        return reverse('books:detail_author', args=[self.pk])

    @property
    def book_amount(self):
        return self.books.count()

    def __str__(self):
        return f'{self.name} {self.surname}'


class Genre(models.Model):
    name = models.CharField(max_length=50)

    @property
    def book_amount(self):
        return self.books.count()

    def get_absolute_url(self):
        return reverse('books:detail_genre', args=[self.pk])

    class Meta:
        ordering = ['name']
        db_table = 'genre'

    def __str__(self):
        return self.name


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
    dict_choices = dict(RATE_CHOICES)

    title = models.CharField(max_length=250)
    author = models.ManyToManyField(Author, related_name='books', blank=True)
    annotation = models.TextField(max_length=500, blank=True, null=True)
    genre = models.ForeignKey(Genre, related_name='books', on_delete=models.SET_NULL,
                              blank=True, null=True)

    rate = models.IntegerField(choices=RATE_CHOICES)

    review = models.TextField(blank=True)

    to_read = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    have_read = models.BooleanField(default=False)

    @property
    def authors(self):
        result = ', '.join([author.__str__() for author in self.author.all()])
        return result

    @property
    def rate_label(self):
        return self.dict_choices[self.rate]

    def get_absolute_url(self):
        return reverse('books:detail_book', args=[self.pk])

    class Meta:
        ordering = ['title']
        db_table = 'book'
