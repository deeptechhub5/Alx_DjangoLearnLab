Authentication System in django_blog
-----------------------------------

How it works:
- Registration: /register/ (uses CustomUserCreationForm to capture username, email, password)
- Login: /login/ (Django's built-in LoginView)
- Logout: /logout/ (Django's built-in LogoutView)
- Profile: /profile/ (view and edit account + profile fields)
- Optional avatar upload stored under MEDIA_ROOT/avatars/

Setup:
1. pip install -r requirements.txt (include Django, Pillow if avatar)
2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py createsuperuser
5. python manage.py runserver

Files added/changed:
- blog/models.py (Profile model)
- blog/forms.py (CustomUserCreationForm, UserUpdateForm, ProfileForm)
- blog/views.py (register, profile)
- blog/urls.py (register/login/logout/profile routes)
- blog/templates/blog/*.html (register, login, logout, profile)
- django_blog/settings.py (LOGIN_REDIRECT_URL, LOGIN_URL, MEDIA settings)
- blog/admin.py (register Profile)

Testing:
- Register a user, login, visit profile, update info, logout. Check admin to see Profile instances.
