📘 Advanced API Project — Django REST Framework

This project is part of the ALX Django LearnLab curriculum. It demonstrates building an advanced REST API using Django REST Framework (DRF), including:

CRUD operations for books

Permissions & user authentication

Filtering, searching, and ordering

DjangoFilterBackend integration

Comprehensive unit testing

API documentation

📂 Project Structure
advanced-api-project/
│
├── api/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── test_views.py
│   └── ...
│
├── advanced_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── manage.py

✨ Features
✔ Full CRUD for Book model

List all books

Retrieve a single book

Create, update, delete (requires authentication)

✔ Permissions

Anyone can list & view book details

Only authenticated users can create, update, or delete

DRF permissions used:

IsAuthenticated, IsAuthenticatedOrReadOnly

✔ Filtering, Searching, Ordering

Supported via query parameters:

Feature	Example
Filter by title	?title=Alpha Book
Search title/author	?search=John
Order by fields	?ordering=title
✔ Unit Tests

Covers:

CRUD operations

Permissions

Filtering

Searching

Ordering

Runs with:

python manage.py test api

📦 Installation & Setup
1. Clone the Repo
git clone <your_repo_url>
cd advanced-api-project

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate  # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Apply Migrations
python manage.py migrate

5. Run Dev Server
python manage.py runserver

🧩 API Endpoints
Books
Method	Endpoint	Description
GET	/api/books/	List all books (supports filtering/searching/ordering)
GET	/api/books/<id>/	Retrieve single book
POST	/api/books/create/	Create book (auth required)
PUT	/api/books/update/<id>/	Update book (auth required)
DELETE	/api/books/delete/<id>/	Delete book (auth required)
🔍 Filtering, Searching & Ordering
✔ Filtering
/api/books/?title=Alpha Book

✔ Searching

Searches title and author__name:

/api/books/?search=Alpha

✔ Ordering

Order by title:

/api/books/?ordering=title


Order by publication year descending:

/api/books/?ordering=-publication_year

🧪 Running Tests

Tests are located in:

api/test_views.py


Run tests:

python manage.py test api


All tests include:

Create book

Update book

Delete book

List & detail

Permissions

Filtering, searching, ordering

🛠 Technology Stack

Python 3.12+

Django 5

Django REST Framework

django-filter

📄 Example Output (List Books Response)
[
  {
    "id": 1,
    "title": "Alpha Book",
    "author": 3,
    "publication_year": 2000
  }
]

📝 Notes

Uses DRF generic class-based views for clean API handling

Strict permission rules ensure secure API usage

Tests run in an isolated in-memory database

Designed to meet all ALX checker requirements

🎉 Completed Requirements

✔ CRUD views
✔ Permissions (IsAuthenticatedOrReadOnly & IsAuthenticated)
✔ URL configuration
✔ Filtering (DjangoFilterBackend)
✔ Searching (SearchFilter)
✔ Ordering (OrderingFilter)
✔ Unit tests for all endpoints
✔ Updated project README