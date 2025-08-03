from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """Form for creating or editing Book instances securely."""
    class Meta:
        model = Book
        fields = ['title', 'author']

class SearchForm(forms.Form):
    """Simple search form for filtering books."""
    query = forms.CharField(max_length=100, required=False, label='Search Books')
