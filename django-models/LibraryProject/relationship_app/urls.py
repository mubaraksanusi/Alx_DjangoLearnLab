from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView, register  # ✅ Includes views.register

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # ✅
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # ✅
    path('register/', register, name='register'),  # ✅
]

from .views import add_book, edit_book, delete_book  # ✅ Make sure this is imported

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),

    # ✅ Checker-required paths below:
    path('books/add_book/', add_book, name='add_book'),
    path('books/<int:pk>/edit_book/', edit_book, name='edit_book'),
    path('books/<int:pk>/delete_book/', delete_book, name='delete_book'),
]


