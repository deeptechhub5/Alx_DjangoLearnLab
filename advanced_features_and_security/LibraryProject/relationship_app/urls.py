from django.urls import path
from .views import list_books, LibraryDetailView
from .views import login_view, logout_view, register_view
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # class-based view
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  # include app URLs
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('book/create/', create_book, name='create_book'),
    path('book/<int:book_id>/edit/', edit_book, name='edit_book'),
    path('book/<int:book_id>/delete/', delete_book, name='delete_book'),
]
