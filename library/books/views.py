from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

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
