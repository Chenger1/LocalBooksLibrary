from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import books.views as views

app_name = 'books'

urlpatterns = [
    path('', views.ListBookView.as_view(), name='list_books'),
    path('is_favorite/', views.ListFavoriteBookView.as_view(), name='list_favorite_books'),
    path('to_read/', views.ListToReadBookView.as_view(), name='list_to_read_books'),
    path('have_read/', views.ListHaveReadBookView.as_view(), name='list_have_read_books'),
    path('authors/', views.ListAuthorView.as_view(), name='list_author'),
    path('author/<int:pk>/', views.DetailAuthorView.as_view(), name='detail_author'),
    path('genres/', views.ListGenreView.as_view(), name='list_genre'),
    path('genre/<int:pk>', views.DetailGenreView.as_view(), name='detail_genre'),
    path('add_new_book/', views.AddNewBookView.as_view(), name='add_new_book'),
    path('detail_book/<int:pk>/', views.DetailBookView.as_view(), name='detail_book'),
    path('add_new_author/', views.AddNewAuthorView.as_view(), name='add_new_author'),
    path('add_new_genre/', views.AddNewGenreView.as_view(), name='add_new_genre'),
    path('update_book/<int:pk>/', views.UpdateBookView.as_view(), name='update_book'),
    path('update_author/<int:pk>/', views.UpdateAuthorView.as_view(), name='update_author'),
    path('update_genre/<int:pk>/', views.UpdateGenreView.as_view(), name='update_genre'),
    path('delete_book/<int:pk>/', views.DeleteBookView.as_view(), name='delete_book'),
    path('delete_author/<int:pk>/', views.DeleteAuthorView.as_view(), name='delete_author'),
    path('delete_genre/<int:pk>/', views.DeleteGenreView.as_view(), name='delete_genre'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
