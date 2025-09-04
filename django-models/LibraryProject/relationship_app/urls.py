from django.urls import path
from .views import list_books, LibraryDetailView

# Urls for relationship app
urlpatterns = [
    path('book-list/', list_books, name='book_list'),
    path('library/', LibraryDetailView.as_view(), name='library'),
]