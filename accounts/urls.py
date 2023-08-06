from .views import register
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('accounts/register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]