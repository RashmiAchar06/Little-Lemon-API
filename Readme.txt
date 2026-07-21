Little Lemon Restaurant API

API Paths for Testing

Home Page
http://127.0.0.1:8000/

Menu API
GET    http://127.0.0.1:8000/menu/
GET    http://127.0.0.1:8000/menu/1/

Booking API
GET    http://127.0.0.1:8000/bookings/
GET    http://127.0.0.1:8000/bookings/1/

Authentication
POST   http://127.0.0.1:8000/api-token-auth/
POST   http://127.0.0.1:8000/auth/users/
POST   http://127.0.0.1:8000/auth/token/login/
POST   http://127.0.0.1:8000/auth/token/logout/

Admin Panel
http://127.0.0.1:8000/admin/

Testing
Run the server:
python manage.py runserver

Run unit tests:
python manage.py test
