from rest_framework import serializers
from .models import Book

class BookViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        feilds = '__all__'