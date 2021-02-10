from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=250, blank=True)
    surname = models.CharField(max_length=250)

    class Meta:
        ordering = ['name']
        db_table = 'author'

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'

    @property
    def book_amount(self):
        return self.books.count()


class Genre(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']
        db_table = 'genre'


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
    annotation = models.TextField(max_length=500, blank=True, null=True)
    genre = models.ForeignKey(Genre, related_name='books', on_delete=models.SET_NULL,
                              blank=True, null=True)

    rate = models.IntegerField(choices=RATE_CHOICES, blank=True)

    review = models.TextField(blank=True)

    to_read = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    have_read = models.BooleanField(default=False)

    @property
    def authors(self):
        result = ', '.join([author.full_name for author in self.author.all()])
        return result

    class Meta:
        ordering = ['title']
        db_table = 'book'
