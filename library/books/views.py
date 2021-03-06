from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import CreateView

from django.urls import reverse_lazy

from books.models import Book, Author, Genre


class ListBookView(ListView):
    model = Book
    template_name = 'book/list_book.html'


class ListFavoriteBookView(ListBookView):
    def get_queryset(self):
        return self.model.objects.filter(is_favorite=True)


class ListToReadBookView(ListBookView):
    def get_queryset(self):
        return self.model.objects.filter(to_read=True)


class ListHaveReadBookView(ListBookView):
    def get_queryset(self):
        return self.model.objects.filter(have_read=True)


class ListAuthorView(ListView):
    model = Author
    template_name = 'author/list_author.html'


class DetailAuthorView(DetailView):
    model = Author
    template_name = 'author/detail_author.html'


class ListGenreView(ListView):
    model = Genre
    template_name = 'genre/list_genre.html'


class DetailGenreView(DetailView):
    model = Genre
    template_name = 'genre/detail_genre.html'


class AddNewBookView(CreateView):
    model = Book
    template_name = 'book/add_new_book.html'
    fields = ['title', 'author', 'genre', 'annotation', 'rate', 'review', 'is_favorite', 'to_read', 'have_read']


class DetailBookView(DetailView):
    model = Book
    template_name = 'book/detail_book.html'


class AddNewAuthorView(CreateView):
    model = Author
    template_name = 'author/add_new_author.html'
    fields = ['name', 'surname']


class AddNewGenreView(CreateView):
    model = Genre
    template_name = 'genre/add_new_genre.html'
    fields = ['name']


class UpdateBookView(UpdateView):
    model = Book
    template_name = 'book/add_new_book.html'
    fields = ['title', 'author', 'genre', 'annotation', 'rate', 'review', 'is_favorite', 'to_read', 'have_read']


class UpdateGenreView(UpdateView):
    model = Genre
    template_name = 'genre/add_new_genre.html'
    fields = ['name']


class UpdateAuthorView(UpdateView):
    model = Author
    template_name = 'author/add_new_author.html'
    fields = ['name', 'surname']


class DeleteBookView(DeleteView):
    model = Book
    success_url = reverse_lazy('books:list_books')


class DeleteGenreView(DeleteView):
    model = Genre
    success_url = reverse_lazy('books:list_genre')


class DeleteAuthorView(DeleteView):
    model = Author
    success_url = reverse_lazy('books:list_author')
