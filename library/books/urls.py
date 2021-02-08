from django.urls import path

import books.views as views

app_name = 'books'

urlpatterns = [
    path('', views.ListBookView.as_view(), name='list_books'),
    path('is_favorite/', views.ListFavoriteBookView.as_view(), name='list_favorite_books'),
    path('to_read/', views.ListToReadBookView.as_view(), name='list_to_read_books'),
]
