from rest_framework import viewsets, permissions, filters, status
from rest_framework.pagination import PageNumberPagination
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response


class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    pagination_class = StandardPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    pagination_class = StandardPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedView(APIView):
    """
    Return posts created by users the authenticated user follows.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        following_qs = user.following.all()

        # If user follows no one, return empty list
        if not following_qs.exists():
            page = []
            return Response({'results': [], 'count': 0})

        posts_qs = Post.objects.filter(author__in=following_qs).order_by('-created_at')
        paginator = FeedPagination()
        page = paginator.paginate_queryset(posts_qs, request)
        serializer = PostSerializer(page, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)