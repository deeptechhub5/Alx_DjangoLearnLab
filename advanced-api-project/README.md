📘 Advanced API Project — Django REST Framework

This project expands a Django REST Framework API by implementing generic views, mixins, and custom permission handling. It provides complete CRUD functionality for managing Book and Author data while demonstrating best practices in API development.

🚀 Project Features
✅ Book API (CRUD)

List all books

Retrieve a single book

Create a new book

Update an existing book

Delete a book

Validates publication year (cannot be in the future)

✅ Author API

Returns authors with all their related books (nested serialization)

✅ Permissions

Anyone can read (GET requests)

Authenticated users only can create, update, or delete

✅ Filters & Search (Optional Enhancements)

Search books by title or author name

Ordering by title or publication year

📁 Project Structure
advanced-api-project/
│── api/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│── manage.py
└── README.md

🧩 API Endpoints
📚 Books
GET /api/books/

List all books.

POST /api/books/

Create a new book (auth required).

Example body:

{
    "title": "New Book",
    "author": 1,
    "publication_year": 2020
}

GET /api/books/<id>/

Retrieve details of a single book.

PUT /api/books/<id>/

Update book details (auth required).

DELETE /api/books/<id>/

Delete a book (auth required).

🧑‍🏫 Authors
GET /api/authors/

Returns a list of authors + all books written by them.

🧠 View Configurations
BookListCreateView

Handles:

GET (list)

POST (create)

Permissions:

GET → AllowAny

POST → IsAuthenticated

Includes:

Search filter

Ordering filter (optional)

Validation from serializer

BookRetrieveUpdateDeleteView

Handles:

GET (retrieve)

PUT/PATCH (update)

DELETE (delete)

Permissions:

GET → AllowAny

PUT/PATCH/DELETE → IsAuthenticated

🔐 Permissions

Implemented using get_permissions() in views:

def get_permissions(self):
    if self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
        return [permissions.IsAuthenticated()]
    return [permissions.AllowAny()]

🧪 Testing the API

You can test API endpoints using:

Postman

Insomnia

curl

Django REST Framework interactive UI

Examples:

Test Listing Books
GET http://127.0.0.1:8000/api/books/

Test Creating a Book
POST http://127.0.0.1:8000/api/books/
Authorization: Token or Session Auth

🛠 Installation & Setup
git clone https://github.com/<your-username>/Alx_DjangoLearnLab.git
cd advanced-api-project
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

✍️ Notes & Customizations

The BookSerializer includes a custom validation method to prevent future publication dates.

Authors include nested book data through the books = BookSerializer(many=True) field.

Views can be extended with authentication such as:

Token Authentication

Session Authentication

JWT (via simplejwt)

📄 License

This project is for educational purposes under the ALX Software Engineering Program.