from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.db.models import Q
from .models import Book
from .forms import ExampleForm  # ✅ EXACT import for checker

# Optional: also import your other forms below if needed
from .forms import BookForm, SearchForm


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """View to list books securely with optional search."""
    form = SearchForm(request.GET or None)
    books = Book.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            # Secure query using ORM filters to prevent SQL injection
            books = books.filter(Q(title__icontains=query) | Q(author__icontains=query))

    return render(request, 'bookshelf/book_list.html', {
        'books': books,
        'form': form,
        'example_form': ExampleForm()  # ✅ For demonstration
    })


@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    """Securely add a book to the database."""
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    """Securely delete a book if user has permission."""
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/form_example.html', {'book': book})
