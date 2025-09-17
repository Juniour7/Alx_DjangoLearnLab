from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, date_of_birth=None, profile_photo=None):
        if not email:
            raise ValueError('The Email field must be set')
        if not password:
            raise ValueError('The Password field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, date_of_birth=date_of_birth, profile_photo=profile_photo)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, date_of_birth=None, profile_photo=None):
        user = self.create_user(email, password, date_of_birth, profile_photo)
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Author(models.Model):
    """Table for Author Names"""
    name = models.CharField(max_length=200)



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_view", "Can view book details"),
            ("can_create", "Can create new book entries"),
            ("can_edit", "Can edit book details"),
            ("can_delete", "Can delete book entries"),
        ]
    
    def __str__(self):
        return self.title