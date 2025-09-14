from django.urls import path
from .views import list_books, LibraryDetailView, SignUpView, LoginView, LogoutView
from .admin_view import admin_view
from .librarian_view import librarian_display
from .member_view import member_display
from . import views


# Urls for relationship app
urlpatterns = [
    path('book-list/', list_books, name='book_list'),
    path('library/', LibraryDetailView.as_view(), name='library'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView, name='logout'),
    path('admin-view/', admin_view, name='admin_view'),

    #Librarian 
    path('librarian-view/', librarian_display, name='librarian_view'),
    path('member-view/', member_display, name='member_view'),

    path("books/", views.book_list, name="book_list"),
    path("books/add/", views.add_book, name="add_book"),
    path("books/edit/<int:book_id>/", views.edit_book, name="edit_book"),
    path("books/delete/<int:book_id>/", views.delete_book, name="delete_book"),
]