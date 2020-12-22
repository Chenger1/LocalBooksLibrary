from django import forms

from books.models import Folder


class AddNewBookForm(forms.Form):
    book_file_path = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    folders = forms.ModelChoiceField(queryset=Folder.objects.all(), empty_label='Nothing')
