from django.urls import path

import books.views as views

app_name = 'books'

urlpatterns = [
    path('', views.ListBookView.as_view(), name='list_books'),
    path('is_favorite/', views.ListFavoriteBookView.as_view(), name='list_favorite_books'),
    path('to_read/', views.ListToReadBookView.as_view(), name='list_to_read_books'),
    path('have_read/', views.ListHaveReadBookView.as_view(), name='list_have_read_books'),
    path('authors/', views.ListAuthorView.as_view(), name='list_author'),
    path('author/<int:pk>/', views.DetailAuthorView.as_view(), name='detail_author'),
]
