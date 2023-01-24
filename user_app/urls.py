from django.urls import path
from .views import get_single_user,register,get_current_user,login,get_all_users
urlpatterns = [
    path('<int:pk>', get_single_user),
    path('all/', get_all_users),
    path('login', login),
    path('register', register),
    path('get-user', get_current_user, name="current_user"),

]