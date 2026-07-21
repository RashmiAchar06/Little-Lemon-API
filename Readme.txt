# Little Lemon Restaurant API

## Project Description
The Little Lemon Restaurant API is a Django REST Framework application that provides RESTful APIs for managing restaurant menu items and table bookings. It also supports user authentication using Django REST Framework Token Authentication and Djoser.

## Technologies Used
- Python
- Django
- Django REST Framework
- MySQL
- Djoser
- Token Authentication

## Installation

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Configure the MySQL database in `settings.py`.
5. Apply migrations:

```bash
python manage.py migrate
```

6. Create a superuser:

```bash
python manage.py createsuperuser
```

7. Start the development server:

```bash
python manage.py runserver
```

## API Endpoints

### Home
```
/
```

### Menu
```
GET    /menu/
POST   /menu/
GET    /menu/<id>/
PUT    /menu/<id>/
DELETE /menu/<id>/
```

### Bookings
```
GET    /bookings/
POST   /bookings/
GET    /bookings/<id>/
PUT    /bookings/<id>/
DELETE /bookings/<id>/
```

### Authentication
```
POST /api-token-auth/
POST /auth/token/login/
POST /auth/token/logout/
POST /auth/users/
```

### Admin Panel
```
/admin/
```

## Running Tests

```bash
python manage.py test
```

## Author

Rashmi Achar