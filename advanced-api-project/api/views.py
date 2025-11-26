from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


"""
Book List & Create View
GET  /books/    → List all books
POST /books/    → Create a new book (authenticated users only)
"""
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Anyone can view, only authenticated can create
    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


"""
Book Detail, Update & Delete View
GET    /books/<pk>/ → Retrieve book
PUT    /books/<pk>/ → Update book (auth only)
DELETE /books/<pk>/ → Delete book (auth only)
"""
class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Auth required for update/delete
    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
