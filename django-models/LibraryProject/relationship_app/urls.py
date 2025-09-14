from django.urls import path
from .views import list_books, LibraryDetailView, SignUpView, LoginView, LogoutView
from .admin_view import admin_view

# Urls for relationship app
urlpatterns = [
    path('book-list/', list_books, name='book_list'),
    path('library/', LibraryDetailView.as_view(), name='library'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin-view/', admin_view, name='admin_view'),
]