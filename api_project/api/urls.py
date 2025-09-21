from django.urls import path, include
from . import views
from .views import BookViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book_list'),
    path('', include('router.urls')),
]