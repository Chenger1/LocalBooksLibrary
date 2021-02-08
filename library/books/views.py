from django.views.generic.list import ListView

from books.models import Book, Author


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
    template_name = 'book/list_author.html'
