from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book

class BookAPITests(APITestCase):

    USERNAME = 'testuser'
    PASSWORD = 'testpassword'

    def setUp(self):
        """Create a user and authenticate"""
        self.user = User.objects.create_user(username=self.USERNAME, password=self.PASSWORD)
        self.token = self.authorize()

        # Add authorization header to the client
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'genre': 'Test Genre',
            'publication_year': 2022,
        }

    def authorize(self):
        """Obtain an authentication token via API"""
        response = self.client.post(
            '/api/token/',
            {'username': self.USERNAME, 'password': self.PASSWORD},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK, "Authorization failed!")
        return response.json().get('access')

    def test_create_book(self):
        """Test book creation"""
        response = self.client.post('/books-lib/books/', self.book_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.book_data['title'])

    def test_get_book_list(self):
        """Test retrieving the book list"""
        Book.objects.create(**self.book_data)

        response = self.client.get('/books-lib/books/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_delete_book(self):
        """Test book deletion"""
        book = Book.objects.create(**self.book_data)

        response = self.client.delete(f'/books-lib/books/{book.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=book.id).exists())

    def test_get_single_book(self):
        """Test retrieving a single book"""
        book = Book.objects.create(**self.book_data)

        response = self.client.get(f'/books-lib/books/{book.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book_data['title'])
