from .views import register, login_user
from django.urls import path

urlpatterns = [
    path('login/', login_user, name="logi"),
    path('register/', register, name='register'),
]