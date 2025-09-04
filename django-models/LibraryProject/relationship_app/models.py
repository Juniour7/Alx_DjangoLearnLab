from django.db import models

# Create your models here.
class AuthorModel(models.Model):
    name = models.CharField(max_length=200)

class BookModel(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)

class LibraryModel(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(BookModel, related_name='books')

class LibrarianModel(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(LibraryModel,on_delete=models.CASCADE )