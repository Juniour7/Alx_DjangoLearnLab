from django.urls import path
from . import views

# Urls for relationship app
urlpatterns = [
    path('book-list/', views.book_list, name='book_list'),
    path('library/', views.Library_Detail.as_view(), name='library'),
]