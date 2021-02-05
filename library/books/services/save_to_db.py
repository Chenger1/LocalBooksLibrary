from typing import  Dict

from books.models import Book, Author


class Saver:

    @staticmethod
    def save_book_to_db(data: Dict[str, str]) -> Book:
        book_inst = Book.objects.create(title=data['name'],
                                        annotation=data.get('annotation'),
                                        genre=data.get('genre'),
                                        rate=1)
        return book_inst
