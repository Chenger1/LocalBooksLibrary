from django.urls import path

import ebooks.views as views


app_name = 'ebooks'


urlpatterns = [
    path('', views.ListEbooksView.as_view(), name='list_top_e-folder'),
    path('<int:dir_id>', views.ListEbooksView.as_view(), name='list_ebooks'),
    path('check_folder_for_update/', views.CheckFoldersUpdate.as_view(), name='check_folder_for_update'),
    path('save_data/', views.CheckFoldersUpdate.as_view(),
         name='save_data'),
    path('add_book/', views.AddNewBook.as_view(), name='add_new_book'),
    path('add_book_with_filedialog/', views.AddNewBook.as_view(), {'open_filedialog': True},
         name='add_new_book_with_filedialog'),
    path('add_book_post/', views.AddNewBook.as_view(), name='add_new_book_post'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('now_found/<str:info_to_display>/', views.NotFoundView.as_view(), name='not_found'),
    path('update_info_about_books/', views.UpdateInfoAboutBooksView.as_view(), name='update_info_about_books'),
]
