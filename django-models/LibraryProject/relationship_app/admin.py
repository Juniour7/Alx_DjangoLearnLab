from django.contrib import admin
from .models import AuthorModel, BookModel, LibrarianModel, LibraryModel

# Register your models here.
admin.site.register(AuthorModel)
admin.site.register(BookModel)
admin.site.register(LibraryModel)
admin.site.register(LibrarianModel)