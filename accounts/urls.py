from .views import register, login_user, CustomLogoutView, CustomLoginView
from django.urls import path

urlpatterns = [
    path('login/', login_user, name="logi"),
    path('register/', register, name='register'),
    # path('accounts/login/', CustomLoginView.as_view(), name='login'),
    # path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
]