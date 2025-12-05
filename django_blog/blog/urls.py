from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    # placeholders for login/register so template url tags can resolve
    path('login/', views.home, name='login'),
    path('register/', views.home, name='register'),
]
