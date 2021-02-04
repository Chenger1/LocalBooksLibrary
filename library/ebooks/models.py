from django.db import models
from django.urls import reverse


class Folder(models.Model):
    name = models.CharField(max_length=250)
    parent_folder = models.ForeignKey('self', on_delete=models.CASCADE, blank=True,
                                      null=True, related_name='subfolders')  # Folder can have subfolders

    size = models.FloatField(max_length=25)

    created = models.DateTimeField()

    is_top_folder = models.BooleanField(default=False)
    path = models.FilePathField()

    def get_absolute_url(self):
        return reverse('ebooks:list_ebooks', args=[self.pk])

    class Meta:
        ordering = ['name']
        db_table = 'folder'

    def __str__(self):
        return self.name


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
    size = models.FloatField(max_length=25)
    path = models.TextField()

    file_creation_time = models.DateTimeField()

    to_read = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    have_read = models.BooleanField(default=False)

    last_read_time = models.DateTimeField(auto_now=True)

    author = models.ManyToManyField(Author, related_name='books', blank=True)
    description = models.TextField(max_length=500, blank=True)
    genre = models.CharField(max_length=50, blank=True)

    rate = models.IntegerField(choices=RATE_CHOICES, blank=True)

    review = models.TextField(blank=True)

    folder = models.ForeignKey(Folder, on_delete=models.CASCADE,
                               related_name='books')

    extension = models.CharField(max_length=20)

    class Meta:
        ordering = ['title']
        db_table = 'book'