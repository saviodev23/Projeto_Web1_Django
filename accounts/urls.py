from .views import register, login_user, listar_notificacoes
from django.urls import path

urlpatterns = [
    path('login/', login_user, name="logi"),
    path('register/', register, name='register'),
    path('notificacoes/', listar_notificacoes, name='listar_notificacoes'),

]