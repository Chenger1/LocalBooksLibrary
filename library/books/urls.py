from django.urls import path

from .views import ListBooksView


app_name = 'books'


urlpatterns = [
    path('', ListBooksView.as_view(), name='list_books'),
]
