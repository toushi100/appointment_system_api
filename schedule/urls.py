from django.urls import path
from .views import *
urlpatterns = [
    path('create/', create, name='create'),
    path('show/<int:pk>/', show, name='show'),
]
