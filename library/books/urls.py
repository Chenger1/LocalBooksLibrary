from django.urls import path

from .views import ListBooksView


app_name = 'books'


urlpatterns = [
    path('', ListBooksView.as_view(), name='list_top_folder'),
    path('<int:dir_id>', ListBooksView.as_view(), name='list_books'),
]
