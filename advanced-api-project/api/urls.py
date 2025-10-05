from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView, name='book-list'),
    path('books/<int:pk>/', views.BookDetailView, name='book_detail-view'),
    path('book-new/', views.BookCreateView, name='create_book'),
    path('book-update/', views.BookUpdateView, name='update_book'),
    path('book-delete/', views.BookDeleteView, name='delete_book'),
]