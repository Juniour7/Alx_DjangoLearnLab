from django.db import models

# Create your models here.
class Author(models.Model):
    """Table for Author Names"""
    name = models.CharField(max_length=200)



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()