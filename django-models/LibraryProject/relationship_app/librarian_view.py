from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import Author, Book, Librarian, Library, UserProfile


def is_librarian(user):
    return user.is_authenticated and user.groups.filter(name="Librarians").exists()

@user_passes_test(is_librarian)
def librarian_display(request):
    context = {
        "Librarians": Librarian.objects.all(),
        "Libraries": Library.objects.all(),
        "Books": Book.objects.all(),
        "Authors": Author.objects.all(),
    }
    return render(request, "relationship_app/librarian_view.html", context)