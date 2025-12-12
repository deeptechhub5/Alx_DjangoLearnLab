Social Media API

A Django REST Framework–powered backend for user management, authentication, and future social media features. This initial build covers full project setup, custom user modeling, registration, login, token generation, and profile management.

Features

Django REST Framework backend

Custom User Model (bio, profile_picture, followers)

Token Authentication using rest_framework.authtoken

User Registration (/register/)

User Login (/login/)

User Profile View & Update (/profile/)

Fully modular accounts app

Project Requirements

Python 3.10+

Django 5+

Django REST Framework

Django REST Framework Authtoken

1. Installation & Environment Setup
1.1 Clone the Repo
git clone https://github.com/YOUR_USERNAME/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api

1.2 Create Virtual Environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

1.3 Install Dependencies
pip install django djangorestframework djangorestframework-authtoken

2. Project Setup

Your project should contain:

social_media_api/ (main project folder)

accounts/ (app for user handling)

2.1 Create Project & App
django-admin startproject social_media_api
cd social_media_api
python manage.py startapp accounts

2.2 Add Apps to INSTALLED_APPS

Inside social_media_api/settings.py add:

INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    'accounts',
]

2.3 Configure Custom User Model

In settings.py:

AUTH_USER_MODEL = 'accounts.User'

3. Models (Custom User Model)

Inside accounts/models.py:

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.URLField(blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    def __str__(self):
        return self.username

4. Serializers

Inside accounts/serializers.py:

from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'bio', 'profile_picture']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        user.bio = validated_data.get('bio', '')
        user.profile_picture = validated_data.get('profile_picture', '')
        user.save()

        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']

5. Views

Inside accounts/views.py:

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

6. URL Routing
6.1 Project URLs

Inside social_media_api/urls.py add:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]

6.2 Accounts App URLs

Create accounts/urls.py:

from django.urls import path
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view()),
]

7. Migrations

Run:

python manage.py makemigrations
python manage.py migrate

8. Running the Server
python manage.py runserver

9. Testing the API (Postman or cURL)
Register

POST /accounts/register/
Body (JSON):

{
  "username": "user1",
  "password": "pass123",
  "email": "user@example.com",
  "bio": "Hello world",
  "profile_picture": "https://example.com/me.jpg"
}


Returns:

{ "token": "generated-token-here" }

Login

POST /accounts/login/

{
  "username": "user1",
  "password": "pass123"
}

Profile

GET /accounts/profile/
Headers:

Authorization: Token your_token_here

10. GitHub Workflow
Initialize Git
git init
git add .
git commit -m "Initial social media API with custom user and token auth"

Push
git remote add origin https://github.com/YOUR_USERNAME/Alx_DjangoLearnLab.git
git push -u origin main

11. Project Structure
social_media_api/
│
├── accounts/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── social_media_api/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│
├── manage.py
└── README.md


### Follow / Unfollow and Feed

- `POST /api/accounts/follow/<user_id>/` — follow the user with id `user_id`.
  - Headers: `Authorization: Token <token>`
  - Example: `POST /api/accounts/follow/2/`

- `POST /api/accounts/unfollow/<user_id>/` — unfollow the user with id `user_id`.
  - Headers: `Authorization: Token <token>`

- `GET /api/accounts/following/` — list users the authenticated user follows.
  - Headers: `Authorization: Token <token>`

- `GET /api/accounts/followers/` — list users that follow the authenticated user.
  - Headers: `Authorization: Token <token>`

- `GET /api/feed/` — get a paginated feed of posts from users the authenticated user follows.
  - Headers: `Authorization: Token <token>`
  - Query params: `page`, `page_size`
  - Example: `GET /api/feed/?page=1&page_size=10`
