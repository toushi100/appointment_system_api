from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create, name='create'),
    path('reserved_incubators/', reserved_incubators, name='reserved_incubators'),
    path('update/<int:pk>/', update, name='update'),
]