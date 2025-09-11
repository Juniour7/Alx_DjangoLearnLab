from django.contrib import admin
from .models import Author, Book, Librarian, Library, UserProfile

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(UserProfile)