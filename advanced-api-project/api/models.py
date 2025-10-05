from django.db import models

# Create your models here.
class Author(models.Model):
    # Author model to store author information
    name = models.CharField(max_length=150)

class Book(models.Model):
    # Book model to store the book inventory
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)