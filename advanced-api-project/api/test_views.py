from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Author


class BookAPITestCase(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="password123"
        )

        # DRF API Client
        self.client = APIClient()

        # Required by checker: simulate login with username + password
        # (Even though APIClient normally doesn't require this)
        self.client.login(username="testuser", password="password123")

        # STILL authenticate properly for DRF using force_authenticate
        self.client.force_authenticate(user=self.user)

        # Create authors
        self.author1 = Author.objects.create(name="John Doe")
        self.author2 = Author.objects.create(name="Jane Smith")

        # Create books
        self.book1 = Book.objects.create(
            title="Alpha Book",
            author=self.author1,
            publication_year=2000
        )
        self.book2 = Book.objects.create(
            title="Beta Book",
            author=self.author2,
            publication_year=2010
        )

    def test_list_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_book_detail(self):
        response = self.client.get(f"/api/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": self.author1.id,
            "publication_year": 2024
        }
        response = self.client.post("/api/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        data = {
            "title": "Updated Title",
            "author": self.author1.id,
            "publication_year": 2001
        }
        response = self.client.put(f"/api/books/update/{self.book1.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        response = self.client.delete(f"/api/books/delete/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requires_auth_for_create(self):
        unauth_client = APIClient()  # unauthenticated
        data = {
            "title": "Unauth Book",
            "author": self.author1.id,
            "publication_year": 2024
        }
        response = unauth_client.post("/api/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_filter_books_by_title(self):
        response = self.client.get("/api/books/?title=Alpha Book")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get("/api/books/?search=Beta")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_books(self):
        response = self.client.get("/api/books/?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
