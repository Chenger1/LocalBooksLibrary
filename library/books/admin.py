from django.contrib import admin

from books.models import Book, Author
from ebooks.models import Ebook


class EbookInline(admin.StackedInline):
    model = Ebook
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'rate']
    list_filter = ['author__surname', 'genre', 'rate', 'have_read', 'to_read', 'is_favorite']
    inlines = [EbookInline]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']
    list_filter = ['name', 'surname']
