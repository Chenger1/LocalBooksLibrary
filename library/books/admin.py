from django.contrib import admin

from .models import Book, Folder


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ['name', 'size', 'is_top_folder']
    list_filter = ['size', 'is_top_folder', 'created']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title']
