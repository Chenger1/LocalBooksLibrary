from django.urls import path

import books.views as views


app_name = 'books'


urlpatterns = [
    path('', views.ListBooksView.as_view(), name='list_top_folder'),
    path('<int:dir_id>', views.ListBooksView.as_view(), name='list_books'),
    path('check_folder_for_update/', views.CheckFoldersUpdate.as_view(), name='check_folder_for_update'),
    path('save_data/', views.CheckFoldersUpdate.as_view(),
         name='save_data'),
    path('add_book/', views.AddNewBook.as_view(), name='add_new_book'),
    path('add_book_with_filedialog/', views.AddNewBook.as_view(), {'open_filedialog': True},
         name='add_new_book_with_filedialog'),
    path('add_book_post/', views.AddNewBook.as_view(), name='add_new_book_post'),
]
