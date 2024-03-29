from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/',create, name='create'),
    path('show/<int:pk>/',show, name='show'),
    path('update/',update, name='update'),
    path('list/',list, name='list'),
    path('index/',index, name='index'),
]