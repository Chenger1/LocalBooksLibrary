from django.db import models
from django.urls import reverse

from books.models import Book


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


class Ebook(models.Model):

    size = models.FloatField(max_length=25)
    path = models.TextField()

    file_creation_time = models.DateTimeField()

    folder = models.ForeignKey(Folder, on_delete=models.CASCADE,
                               related_name='books')

    extension = models.CharField(max_length=20)

    base_book = models.ForeignKey(Book, related_name='ebook', on_delete=models.CASCADE)

    class Meta:
        ordering = ['size']
        db_table = 'ebook'
