from rest_framework import serializers
from .models import Book
from rest_framework import viewsets

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        feilds = '__all__'