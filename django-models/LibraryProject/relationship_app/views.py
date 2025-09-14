from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

# User registration
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login  ,logout

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

class LoginView(login):
    template_name = 'relationship_app/login.html'

class LogoutView(logout):
    template_name = 'relationship_app/logout.html'


def list_books(request):
    # Get books from the database
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books' : books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    fields = ['name', 'books']  