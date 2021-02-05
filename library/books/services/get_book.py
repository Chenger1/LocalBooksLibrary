from typing import Union

from books.models import Book

from django.core.exceptions import ObjectDoesNotExist


def get_book_instance_by_title(title: str) -> Union[Book, None]:
    try:
        book_ins = Book.objects.get(title__iexact=title)
    except ObjectDoesNotExist:
        return None
    else:
        return book_ins
