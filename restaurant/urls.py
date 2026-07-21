from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import MenuViewSet, BookingViewSet, home

router = DefaultRouter()
router.register('menu', MenuViewSet)
router.register('bookings', BookingViewSet)

urlpatterns = [
    path('', home),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]