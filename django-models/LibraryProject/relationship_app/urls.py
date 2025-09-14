from django.urls import path
from .views import (
    list_books, LibraryDetailView,
    SignUpView, LoginView, LogoutView,
    admin_view, librarian_view, member_display,
    add_book, edit_book, delete_book
)

urlpatterns = [
    # Books
    path('books/', list_books, name='book_list'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/', edit_book, name='edit_book'),
    path('delete_book//', delete_book, name='delete_book'),

    # Library
    path('library/', LibraryDetailView.as_view(), name='library'),

    # Auth
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView, name='logout'),

    # Role-based views
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_display, name='member_view'),
]
