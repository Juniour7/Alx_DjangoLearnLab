from django.contrib.auth.decorators import permission_required

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView as AuthLoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .models import Author, Book, Librarian, Library


# --- Book CRUD with permissions ---
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        Book.objects.create(title=title, author=author)
        return redirect("book_list")
    return render(request, "relationship_app/add_book.html")


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.save()
        return redirect("book_list")
    return render(request, "relationship_app/edit_book.html", {"book": book})


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "relationship_app/delete_book.html", {"book": book})


# --- Role check functions ---
def is_member(user):
    return user.is_authenticated and user.groups.filter(name="Members").exists()

def is_librarian(user):
    return user.is_authenticated and user.groups.filter(name="Librarians").exists()

def is_admin(user):
    return user.is_authenticated and user.is_staff


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


# --- Auth views ---
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'


class LoginView(AuthLoginView):
    template_name = 'relationship_app/login.html'


def LogoutView(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')


# --- Book list + Library detail ---
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    fields = ['name', 'books']
