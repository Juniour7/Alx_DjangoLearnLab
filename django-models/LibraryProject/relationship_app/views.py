from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library
from django.views.generic import ListView, DetailView

# Create your views here.
def book_list(request):
    # Get books from the database
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books' : books})

class Library_Detail(ListView):
    model = Library
    template_name = 'library_detail.html'
    fields = ['name', 'books']  