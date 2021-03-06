from typing import Dict

from books.models import Book, Author, Genre


class Saver:

    @staticmethod
    def save_book_to_db(data: Dict[str, str]) -> Book:
        book_inst = Book.objects.create(title=data['name'],
                                        annotation=data.get('annotation'),
                                        genre=data.get('genre'),
                                        rate=1)
        return book_inst

    @classmethod
    def add_author_to_db(cls, author_data: Dict[str, str]) -> Author:
        author_ins, is_created = Author.objects.get_or_create(name=author_data['name'], surname=author_data['surname'])
        return author_ins

    @classmethod
    def add_or_get_genre(cls, genre: str) -> Genre:
        genre_inst, _ = Genre.objects.get_or_create(name=genre)
        return genre_inst

    @classmethod
    def update_book_info(cls, book: Book, info_to_update: Dict[str, str]):
        author_data = {}
        for author in info_to_update['author']:
            temp = author.split(' ')
            author_data['name'], author_data['surname'] = temp[0], temp[-1]
            author = cls.add_author_to_db(author_data)
            book.author.add(author)
        if info_to_update.get('genre'):
            book.genre = cls.add_or_get_genre(info_to_update.get('genre'))
        book.description = info_to_update.get('annotation')
        book.save()
