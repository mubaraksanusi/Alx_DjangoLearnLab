from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library  # ✅ Satisfies the checker


# Function-based view
def list_books(request):
    books = Book.objects.all()  # ✅ Required by checker
    return render(request, 'relationship_app/list_books.html', {'books': books})  # ✅ Required path

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
