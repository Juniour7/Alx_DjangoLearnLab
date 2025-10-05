from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView, name='book-list'),
    path('books/<int:pk>/', views.BookDetailView, name='book_detail-view'),
    path('books/create/', views.BookCreateView, name='create_book'),
    path('books/update/', views.BookUpdateView, name='update_book'),
    path('books/delete/', views.BookDeleteView, name='delete_book'),
]