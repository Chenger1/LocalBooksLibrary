from django import forms

from ebooks.models import Folder


class AddNewBookForm(forms.Form):
    folders = forms.ModelChoiceField(queryset=Folder.objects.all(), empty_label='Nothing')


class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ('name', 'parent_folder')

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data['parent_folder']:
            cleaned_data['parent_folder'] = Folder.objects.get(is_top_folder=True)
        return cleaned_data
