from django.contrib import admin
from .models import Book, Author, CustomUser

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'publication_year')
    list_filter = ('title','author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth')
    list_filter = ('username', 'email', 'date_of_birth')

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(CustomUser, CustomUserAdmin)