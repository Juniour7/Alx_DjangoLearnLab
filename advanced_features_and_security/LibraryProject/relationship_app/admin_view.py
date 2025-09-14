from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import Author, Book, Librarian, Library, UserProfile


@user_passes_test(lambda u: u.is_superuser)
def admin_view(request):
    if not request.user.is_superuser:
        return HttpResponse("You are not an authrized user.")
    
    Authors = Author.objects.all()
    Books = Book.objects.all()  
    Librarians = Librarian.objects.all()
    Libraries = Library.objects.all()       
    UserProfiles = UserProfile.objects.all()

    context = {
        "Authors": Authors,
        "Books": Books,
        "Librarians": Librarians,
        "Libraries": Libraries,
        "UserProfiles": UserProfiles,
    }

    return render(request, 'relationship_app/admin_view.html', context)