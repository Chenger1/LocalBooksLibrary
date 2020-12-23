from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect

from books.utils.structure_manager import StructureManager
from books.utils.subfolders_utils import get_folders

from books.services.save_data_to_db import Saver

from book_finder.services.finder import Finder

from books.forms import AddNewBookForm

from tkinter import Tk, filedialog


class ListBooksView(View):
    template = 'books/list.html'

    def get(self, request, dir_id=None):
        if dir_id:
            folder = get_folders(folder_id=dir_id)
        else:
            folder = get_folders(is_top_folder=True)

        if folder:
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
        else:
            return render(request, self.template, {'folder': None})


class CheckFoldersUpdate(View):
    def get(self, request):
        folder_path = get_folders(is_top_folder=True).path
        if folder_path:
            Saver.clear_folders_structure()
            self.save_folders(folder_path)

        return redirect('books:list_top_folder')

    def post(self, request):
        self.save_folders(request.POST['folder_path'])
        return redirect('books:list_top_folder')

    @staticmethod
    def save_folders(folder_path: str):
        directory = Finder.find_books_in_system(folder_path)
        Saver.save_structure_to_db(directory)


class AddNewBook(View):
    template = 'books/add_book.html'

    def get(self, request, open_filedialog=False):
        books = None
        if open_filedialog:
            tk = Tk()
            tk.attributes('-topmost', True)
            tk.withdraw()
            books = filedialog.askopenfilenames()
            tk.destroy()

        form = AddNewBookForm()

        return render(request, self.template, {'form': form,
                                               'books': books})
