from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User

from .models import Author, Book


class BookAPITestCase(APITestCase):
    """Test suite for Book API endpoints."""

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create author
        self.author = Author.objects.create(name="J.R.R. Tolkien")

        # Create some books
        self.book1 = Book.objects.create(title="The Hobbit", publication_year=1937, author=self.author)
        self.book2 = Book.objects.create(title="The Lord of the Rings", publication_year=1954, author=self.author)

        # API client
        self.client = APIClient()

        # URLs
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book1.id])
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', args=[self.book1.id])
        self.delete_url = reverse('book-delete', args=[self.book1.id])
    

    def test_list_books(self):
        """Test retrieving all books (should be public)."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_retrieve_single_book(self):
        """Test retrieving a single book (should be public)."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "The Hobbit")
    

    def test_create_book_requires_authentication(self):
        """Test that unauthenticated users cannot create a book."""
        data = {'title': 'Silmarillion', 'publication_year': 1977, 'author': self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        """Test that authenticated users can create a book."""
        self.client.login(username='testuser', password='testpass')
        data = {'title': 'Silmarillion', 'publication_year': 1977, 'author': self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book_authenticated(self):
        """Test that authenticated users can update a book."""
        self.client.login(username='testuser', password='testpass')
        data = {'title': 'The Hobbit (Updated)', 'publication_year': 1937, 'author': self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'The Hobbit (Updated)')

    def test_delete_book_authenticated(self):
        """Test that authenticated users can delete a book."""
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_title(self):
        """Test filtering books by title."""
        response = self.client.get(self.list_url, {'title': 'The Hobbit'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'The Hobbit')

    def test_search_books_by_author(self):
        """Test searching books by author name."""
        response = self.client.get(self.list_url, {'search': 'Tolkien'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any('Tolkien' in b['author'] for b in response.data))

    def test_order_books_by_publication_year(self):
        """Test ordering books by publication year."""
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))


