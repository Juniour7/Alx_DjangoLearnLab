from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# My serializers
class BookSerializer(serializers.ModelSerializer):
    # Reveleas the book details
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'publication_year',
            'author'
        ]

    # Publication_year validation
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError('Publication year cannot be in the future')
        return value

class AuthorSerializer(serializers.ModelSerializer):
    # Reveals the author information and their books
    books = BookSerializer(many=True, read_only=True) # this is a nested serializer
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']