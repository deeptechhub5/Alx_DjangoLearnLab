from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    PostsByTagView,
    SearchResultsView,
)

urlpatterns = [
    path('', views.home, name='home'),

    # Better: keep only the class-based list view
    path('posts/', PostListView.as_view(), name='post-list'),

    # Registration / profile
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # Login / Logout
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # REQUIRED BY CHECKER
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comments (CHECKER REQUIRED)
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # Tags
    path('tags/<str:tag_name>/', PostsByTagView.as_view(), name='posts_by_tag'),

    # Search
    path('search/', SearchResultsView.as_view(), name='search'),
]
