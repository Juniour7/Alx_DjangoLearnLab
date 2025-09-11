from django.urls import path
from .views import list_books, LibraryDetailView, SignUpView
from django.contrib.auth.views import LoginView, LogoutView

# Urls for relationship app
urlpatterns = [
    path('book-list/', list_books, name='book_list'),
    path('library/', LibraryDetailView.as_view(), name='library'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]