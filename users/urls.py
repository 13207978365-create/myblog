from django.urls import path

from users import views

urlpatterns = [
    path('user_register', views.user_register, name='user_register'),  #注册
]