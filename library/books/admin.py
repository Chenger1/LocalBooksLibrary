from django.contrib import admin

from .models import Book, Folder, Author


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ['name', 'size', 'is_top_folder']
    list_filter = ['size', 'is_top_folder', 'created']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'pk']
    list_filter = ['extension']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']
