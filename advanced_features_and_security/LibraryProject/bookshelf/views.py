from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from .models import Book
from django.contrib.auth.decorators import  permission_required


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """This displays all the boojs within the database for the permission can_view"""
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# View reuires can_create permission
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        Book.objects.create(title=title, author=author, publication_year = publication_year)
        return redirect('book_list')
    return render(request, 'articles/create.html')
    
# View to edit the already existing books
@permission_required('bookshelf.can_edit', raise_exception= True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        return redirect('book_list')
    return render(request, 'bookshelf/edit.html', {'book': book})

# View to delete a book
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/delete.html', {'book': book})