Little Lemon Restaurant API

Overview
This project is a RESTful API built using Django REST Framework for the Meta Back-End Developer Capstone. It provides APIs to manage restaurant menu items and table bookings, with user authentication and MySQL database integration.

 Technologies
- Python
- Django
- Django REST Framework
- MySQL
- Djoser
- Token Authentication

 API Endpoints

# Home
/
```
GET /
```

# Menu
```
GET    /menu/
POST   /menu/
GET    /menu/<id>/
PUT    /menu/<id>/
DELETE /menu/<id>/
```

# Bookings
```
GET    /bookings/
POST   /bookings/
GET    /bookings/<id>/
PUT    /bookings/<id>/
DELETE /bookings/<id>/
```

# Authentication
```
POST /api-token-auth/
POST /auth/users/
POST /auth/token/login/
POST /auth/token/logout/
```

# Admin
```
/admin/
```

 Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Run the server:

```bash
python manage.py runserver
```

Run tests:

```bash
python manage.py test
```

 Author

Rashmi Achar
