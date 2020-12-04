from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404

from .models import Folder


class ListBooksView(View):
    template = 'books/list.html'

    def get(self, request, dir_id=None):
        if dir_id:
            folder = get_object_or_404(Folder, id=dir_id)
        else:
            folder = get_object_or_404(Folder, is_top_folder=True)

        subdirs = folder.subfolders.get_queryset().all()
        books = folder.books.get_queryset().all()

        return render(request, self.template, {'folder': folder,
                                               'subdirs': subdirs,
                                               'books': books})
