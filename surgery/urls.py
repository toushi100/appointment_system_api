from django.urls import path
from .views import *
 

urlpatterns = [
    path('index_past/', index_past, name='index_past'),
    path('index_upcoming/', index_upcoming, name='index_upcoming'),
    path('create/', create, name='create'),
]