from django.urls import path

import books.views as views

app_name = 'books'

urlpatterns = [
    path('', views.ListBookView.as_view(), name='list_books'),
]