from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # class-based view
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  # include app URLs
]
