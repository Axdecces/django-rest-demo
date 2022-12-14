from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet,basename="user")
router.register(r'addresses', views.AddressViewSet,basename="address")

urlpatterns = [
    path('', include(router.urls)),
]