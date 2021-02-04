from django import forms

from ebooks.models import Folder


class AddNewBookForm(forms.Form):
    folders = forms.ModelChoiceField(queryset=Folder.objects.all(), empty_label='Nothing')
