from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404

from .models import Folder

from books.utils.structure_manager import StructureManager
from books.utils.subfolders_utils import get_folders


class ListBooksView(View):
    template = 'books/list.html'

    def get(self, request, dir_id=None):
        if dir_id:
            folder = get_object_or_404(Folder, id=dir_id)
        else:
            folder = get_object_or_404(Folder, is_top_folder=True)

        StructureManager.update_level(folder.pk, folder.parent_folder_id)

        subdirs = folder.subfolders.get_queryset().all()
        books = folder.books.get_queryset().all()

        parent_folder_id, next_folder_id = StructureManager.get_folders(folder.pk)

        parent_folder = get_folders(parent_folder_id)
        next_folder = get_folders(next_folder_id)

        return render(request, self.template, {'folder': folder,
                                               'subdirs': subdirs,
                                               'books': books,
                                               'parent_folder': parent_folder,
                                               'next_folder': next_folder
                                               })
