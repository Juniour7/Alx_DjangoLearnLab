from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Author, Book, Librarian, Library
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import  permission_required

# User registration
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


#Add Book
@permission_required('relationship_app.can_view_member_page', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        Book.objects.create(title=title, author=author)
        return redirect("book_list")
    return render(request, "relationship_app/add_book.html")

#Edit Book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.save()
        return redirect("book_list")
    return render(request, "relationship_app/edit_book.html", {"book": book})


# --- Role check functions ---
def is_member(user):
    return user.is_authenticated and user.groups.filter(name="Members").exists()

def is_librarian(user):
    return user.is_authenticated and user.groups.filter(name="Librarians").exists()

def is_admin(user):
    return user.is_authenticated and user.is_staff  # or check a "Admins" group if you created one


# --- Member view ---
@user_passes_test(is_member, login_url="/not-authorized/")
def member_display(request):
    context = {
        "librarians": Librarian.objects.all(),
        "libraries": Library.objects.all(),
        "books": Book.objects.all(),
        "authors": Author.objects.all(),
    }
    return render(request, "relationship_app/member_view.html", context)


# --- Librarian view ---
@user_passes_test(is_librarian, login_url="/not-authorized/")
def librarian_view(request):
    context = {
        "librarians": Librarian.objects.all(),
        "libraries": Library.objects.all(),
        "books": Book.objects.all(),
        "authors": Author.objects.all(),
    }
    return render(request, "relationship_app/librarian_view.html", context)


# --- Admin view ---
@user_passes_test(is_admin, login_url="/not-authorized/")
def admin_view(request):
    context = {
        "librarians": Librarian.objects.all(),
        "libraries": Library.objects.all(),
        "books": Book.objects.all(),
        "authors": Author.objects.all(),
    }
    return render(request, "relationship_app/admin_view.html", context)

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

def LogoutView(request):
    return render(request, 'relationship_app/logout.html')


class LoginView(AuthenticationForm):
    template_name = 'relationship_app/login.html'



def list_books(request):
    # Get books from the database
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books' : books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    fields = ['name', 'books']  