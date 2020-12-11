from django.urls import path

import books.views as views


app_name = 'books'


urlpatterns = [
    path('', views.ListBooksView.as_view(), name='list_top_folder'),
    path('<int:dir_id>', views.ListBooksView.as_view(), name='list_books'),
    path('check_folder_for_update/', views.CheckFoldersUpdate.as_view(), name='check_folder_for_update'),
]
