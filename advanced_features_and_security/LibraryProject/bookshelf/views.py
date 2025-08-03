from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from django import forms

# ✅ Secure form for adding books
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

# ✅ Secure search form
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)

# ✅ View for listing books with search
@permission_required('bookshelf.view_book', raise_exception=True)
def book_list(request):
    form = SearchForm(request.GET or None)
    books = Book.objects.all()
    if form.is_valid():
        query = form.cleaned_data['query']
        books = books.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})

# ✅ Create Book (CSRF protected)
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

# ✅ Delete Book
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/form_example.html', {'form': None, 'book': book})
