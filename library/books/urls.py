from django.urls import path

import books.views as views

app_name = 'books'

urlpatterns = [
    path('', views.ListBookView.as_view(), name='list_books'),
    path('is_favorite/', views.ListFavoriteBookView.as_view(), name='list_favorite_books'),
]
