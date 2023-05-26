from django.urls import path    
from .views import *

urlpatterns = [
path('show/<int:pk>/', show, name='show'),
path('create/', create, name='create'),
path('index/', index, name='index'),
]
