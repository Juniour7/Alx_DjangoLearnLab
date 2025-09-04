from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

# Create your views here.
def book_list(request):
    # Get books from the database
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books' : books})

class Library_Detail(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    fields = ['name', 'books']  