from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, viewsets, permissions

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # public list endpoint


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # restrict CRUD to logged-in users