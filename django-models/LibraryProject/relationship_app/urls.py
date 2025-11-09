from django.urls import path
from .views import list_books, LibraryDetailView
from .views import login_view, logout_view, register_view

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # class-based view
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  # include app URLs
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]
