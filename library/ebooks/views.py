from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect

from ebooks.utils.structure_manager import StructureManager
from ebooks.utils.subfolders_utils import get_folders, get_books

from ebooks.services.save_data_to_db import Saver

from book_finder.services.finder import Finder

from ebooks.forms import AddNewBookForm
from ebooks.models import Extension

from books.services.save_to_db import Saver as sv

from common.system_data import move_file_to_folder
from fb2_parser.parser import define_fb2_parser
from epub_parser.parser import EpubParser

from tkinter import Tk, filedialog


class ListEbooksView(View):
    """Displays all ebooks"""
    template = 'books/e-books/ebook_list.html'

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

            folder_nesting = list(reversed(StructureManager.get_full_folder_nesting(folder)))

            return render(request, self.template, {'folder': folder,
                                                   'subdirs': subdirs,
                                                   'books': books,
                                                   'parent_folder': parent_folder,
                                                   'next_folder': next_folder,
                                                   'folder_nesting': folder_nesting
                                                   })
        else:
            return render(request, self.template, {'folder': None})


class CheckFoldersUpdate(View):
    def get(self, request):
        folder_path = get_folders(is_top_folder=True).path
        if folder_path:
            Saver.clear_folders_structure()
            self.save_folders(folder_path)

        return redirect('ebooks:list_top_e-folder')

    def post(self, request):
        self.save_folders(request.POST['folder_path'])
        return redirect('ebooks:list_top_e-folder')

    @staticmethod
    def save_folders(folder_path: str):
        directory = Finder.find_books_in_system(folder_path)
        Saver.save_structure_to_db(directory)


class AddNewBook(View):
    template = 'books/e-books/add_book.html'

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

    def post(self, request):
        folder = get_folders(request.POST['folders'])
        books = request.POST.getlist('books')

        for book in books:
            new_book_path = move_file_to_folder(book, folder.path)
            book = Finder.create_book_instance(new_book_path)
            Saver.save_book_in_folder(book, folder)

        return redirect('ebooks:list_top_e-folder')


class SearchView(View):
    def post(self, request):
        search_query = request.POST['search_query']
        folder = get_folders(folder_name=search_query)
        if folder:
            return redirect('ebooks:list_ebooks', dir_id=folder.pk)
        else:
            return redirect('ebooks:not_found', info_to_display=search_query)


class NotFoundView(View):
    template = 'not_found.html'

    def get(self, request, info_to_display):
        return render(request, self.template, {'info_to_display': info_to_display})


class UpdateInfoAboutBooksView(View):
    def get(self, request):
        for ebook in get_books(all_books=True):  # Get all the Books (Not Ebook instances. Regular Book)
            if ebook.extension.name == 'fb2':
                parser = define_fb2_parser(ebook.path)
            elif ebook.extension.name == 'epub':
                parser = EpubParser(ebook.path)
            else:
                continue

            if parser:
                book_info = parser.get_info_about_book()
                sv.update_book_info(ebook.base_book, book_info)

        return redirect('ebooks:list_top_e-folder')


class ListExtensionsView(ListView):
    model = Extension
    template_name = 'books/e-books/list_extensions.html'


class DetailExtensionView(DetailView):
    model = Extension
    template_name = 'books/e-books/detail_extension.html'
