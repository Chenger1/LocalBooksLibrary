from django.views.generic.list import ListView

from books.models import Book


class ListBookView(ListView):
    model = Book
    template_name = 'book/list_book.html'
