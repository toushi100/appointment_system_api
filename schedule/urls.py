from django.urls import path
from .views import *
urlpatterns = [
    path('create/', create, name='create'),
    path('show/<int:pk>/', show, name='show'),
    path('reserve/<int:pk>/', reserve, name='reserve'),
    path('list_available/<int:doctor_id>/', list_available, name='list_available'),
    path('list_reserved/', list_reserved, name='list_reserved'),
]
